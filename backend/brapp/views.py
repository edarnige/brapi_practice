from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
 #authentication_classes = (BasicAuthentication)
 #permission_classes = (IsAuthenticated)
 queryset = Task.objects.all()
 serializer_class = TaskSerializer

