from rest_framework import serializers

from . import models

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Task
        fields = ('id','description', 'status')


class Trial_TrialContactSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source='contactDbId.name')
    # instituteName = serializers.CharField(source='contactDbId.instituteName')
    # email = serializers.CharField(source='contactDbId.email')
    # type = serializers.CharField(source='contactDbId.type')
    # orcid = serializers.CharField(source='contactDbId.orcid')

    class Meta:
        model = models.Contact
        fields = ('contactDbId', 'name', 'instituteName', 'email', 'type', 'orcid')


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Program
        safe = False
        exclude = ('cropDbId',)