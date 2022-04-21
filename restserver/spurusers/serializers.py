from rest_framework import serializers
from .models import Spurusers

class SpurusersSerializer(serializers.ModelSerializer):
    org_id = serializers.FloatField()
    name = serializers.CharField(max_length=200)
    name =serializers.CharField(max_length=200)

    class Meta:
        model = Spurusers
        fields = ('__all__')