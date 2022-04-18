from rest_framework import serializers
from .models import Tutorials

class TutorialsSerializer(serializers.ModelSerializer):
    org_id = serializers.FloatField()
    name = serializers.CharField(max_length=200)
    name =serializers.CharField(max_length=200)

    class Meta:
        model = Tutorials
        fields = ('__all__')