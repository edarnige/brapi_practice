from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Task, Contact
from .serializers import TaskSerializer, Trial_TrialContactSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
 #authentication_classes = (BasicAuthentication)
 #permission_classes = (IsAuthenticated)
 queryset = Task.objects.all()
 serializer_class = TaskSerializer

class ContactViewSet(viewsets.ModelViewSet):
 queryset = Contact.objects.all()
 serializer_class = Trial_TrialContactSerializer
