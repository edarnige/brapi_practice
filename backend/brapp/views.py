from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Task, Contact, Program
from .serializers import TaskSerializer, Trial_TrialContactSerializer, ProgramSerializer

import json
from ast import literal_eval
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, View
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.core.exceptions import FieldDoesNotExist
#from django_extensions.management.commands import show_urls
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    #authentication_classes = (BasicAuthentication)
    #permission_classes = (IsAuthenticated)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = Trial_TrialContactSerializer

###########TEST

DEF_PAGE_SIZE = 1000
HTTP_BAD_REQUEST_CODE = 400
JSON_POST_ARGS = 'jsonparams'


class JSONResponseMixin(object):
    pagination_params = ['page', 'pageSize']

    def buildErrorResponse(self, message, code):
        err = {"metadata": {
                "pagination": {
                    "pageSize": 0,
                    "currentPage": 0,
                    "totalCount": 0,
                    "totalPages": 0
                },
                "status": [{
                    "message": message,
                    "code": code
                }],
                "datafiles": []
            },
            "result": {}
        }
        return err

    def buildResponse(self, results, pagination={"pageSize": 0, "currentPage": 0, "totalCount": 0, "totalPages": 0}, status=[], datafiles=[]):
        output = {}
        output['result'] = results
        output['metadata'] = {}
        output['metadata']['pagination'] = pagination
        output['metadata']['status'] = status
        output['metadata']['datafiles'] = datafiles
        return output

    def prepareResponse(self, objects, requestDict):
        try:
            pagesize = int(requestDict.get('pageSize', DEF_PAGE_SIZE))
            page = int(requestDict.get('page', 0)) + 1  # BRAPI wants zero page indexing...
        except:
            return self.buildErrorResponse('Invalid page or pageSize parameter', HTTP_BAD_REQUEST_CODE)

        # order is mandatory because of pagination
        if self.model and not objects.ordered:
            objects = objects.order_by('pk')

        paginator = Paginator(objects, pagesize)
        try:
            pageObjects = paginator.page(page)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            return self.buildErrorResponse('Empty page was requested: {}'.format(page-1), HTTP_BAD_REQUEST_CODE)
            # pageObjects = paginator.page(paginator.num_pages)
        pagination = {'pageSize': pagesize,
                      'currentPage': page-1,
                      'totalCount': len(objects),
                      'totalPages': paginator.num_pages
                      }

        # return serialized data
        data = []
        for obj in pageObjects:
            if self.serializer:
                data.append(self.serializer(obj).data)
            else:
                data.append(obj)
        return self.buildResponse(results={'data': data}, pagination=pagination)

    def sortOrder(self, requestDict, objects):
        val = requestDict.get('sortOrder')
        if val is not None:
            val = val.lower()
            if val == 'desc':
                objects = objects.reverse()
            elif val == 'asc':
                pass  # by default
            else:
                raise ValueError('Invalid value for "sortOrder" parameter: {}'.format(val))
        return objects



class GET_response(JSONResponseMixin):
    def checkGETparameters(self, requestDict):
        return set(requestDict.keys()) - set(self.get_parameters) - set(self.pagination_params)

    def get(self, request, *args, **kwargs):
        requestDict = self.request.GET

        # sanity: fail if there are unwanted parameters
        unknownParams = self.checkGETparameters(requestDict)
        if unknownParams:
            return JsonResponse(self.buildErrorResponse('Invalid query pararameter(s) {}'.format(unknownParams), HTTP_BAD_REQUEST_CODE))

        # execute query and make pagination
        objects = self.get_objects_GET(requestDict)
        # try:
        #     objects = self.get_objects_GET(requestDict)
        # except Exception as e:
        #     return JsonResponse(self.buildErrorResponse('Data error: {}'.format(str(e)), HTTP_BAD_REQUEST_CODE))

        response = self.prepareResponse(objects, requestDict)
        return JsonResponse(response)


class POST_JSON_response(JSONResponseMixin):
    def checkPOSTparameters(self, requestDict):
        return set(requestDict.keys()) - set(self.post_json_parameters) - set(self.pagination_params)

    def post(self, request, *args, **kwargs):
        try:
            requestDict = json.loads(request.body.decode("utf-8"))
        except Exception:
            return JsonResponse(self.buildErrorResponse('Invalid JSON POST parameters', HTTP_BAD_REQUEST_CODE))

        unknownParams = self.checkPOSTparameters(requestDict)
        if unknownParams:
            return JsonResponse(self.buildErrorResponse('Invalid query pararameter(s) {}'.format(unknownParams), HTTP_BAD_REQUEST_CODE))

        # execute query and make pagination
        try:
            objects = self.get_objects_POST(requestDict)
        except Exception as e:
            return JsonResponse(self.buildErrorResponse('Data error: {}'.format(str(e)), HTTP_BAD_REQUEST_CODE))

        response = self.prepareResponse(objects, requestDict)
        return JsonResponse(response)


class GET_URLPARAMS_response(JSONResponseMixin):
    def checkGETparameters(self, requestDict):
        return set(requestDict.keys()) - set(self.get_parameters) - set(self.pagination_params)

    def get(self, request, *args, **kwargs):
        requestDict = self.request.GET

        # sanity: fail if there are unwanted parameters
        unknownParams = self.checkGETparameters(requestDict)
        if unknownParams:
            return JsonResponse(self.buildErrorResponse('Invalid query pararameter(s) {}'.format(unknownParams), HTTP_BAD_REQUEST_CODE))

        # execute query and make pagination
        try:
            objects = self.get_objects_GET(requestDict, **kwargs)
        except Exception as e:
            return JsonResponse(self.buildErrorResponse('Data error: {}'.format(str(e)), HTTP_BAD_REQUEST_CODE))

        response = self.prepareResponse(objects, requestDict)
        return JsonResponse(response)


class GET_detail_response(JSONResponseMixin):
    def get(self, request, *args, **kwargs):
        requestDict = kwargs
        try:
            pkval = requestDict.get(self.pk)
            obj = self.model.objects.get(pk=pkval)
        except self.model.DoesNotExist:
            return JsonResponse(self.buildErrorResponse('Invalid object ID', 404))

        serializer = self.serializer(obj)
        return JsonResponse(self.buildResponse(results=serializer.data))


#page using Django templates
class Index(TemplateView):
    template_name = 'root.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return self.get(request)


class ProgramList(GET_response, TemplateView): #replace templateview with viewset?
    model = Program
    serializer = ProgramSerializer
    get_parameters = ['programName', 'abbreviation']

    def get_objects_GET(self, requestDict):
        query = Q()
        if 'programName' in requestDict:
            query &= Q(name=requestDict['programName'])
        if 'abbreviation' in requestDict:
            query &= Q(abbreviation=requestDict['abbreviation'])

        objects = self.model.objects.filter(query)
        return objects