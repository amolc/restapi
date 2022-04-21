from rest_framework import serializers
from .models import Appusers

class AppusersSerializer(serializers.ModelSerializer):
    org_id = serializers.FloatField()
    name = serializers.CharField(max_length=200)
    name =serializers.CharField(max_length=200)

    class Meta:
        model = Appusers
        fields = ('__all__')