from rest_framework import serializers
from .models import Supercategory

class SupercategorySerializer(serializers.ModelSerializer):
    org_id = serializers.FloatField()
    name = serializers.CharField(max_length=200)
    name =serializers.CharField(max_length=200)

    class Meta:
        model = Supercategory
        fields = ('__all__')