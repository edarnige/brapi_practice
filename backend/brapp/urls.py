from django.urls import path
from django.conf.urls import include

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename="task")
router.register('contacts', ContactViewSet, basename="contact")

urlpatterns = [
    path('', include(router.urls)),
    path('testing/', Index.as_view()),
    path('programs', ProgramList.as_view()),
]