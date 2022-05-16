from rest_framework import serializers
from .models import Items

class ItemsSerializer(serializers.ModelSerializer):
    org_id = serializers.FloatField()
    name =serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    price = serializers.CharField(max_length=200)
    currency = serializers.CharField(max_length=200)
    thumbnail = serializers.CharField(max_length=200)
    picture = serializers.CharField(max_length=200)
    longtext = serializers.CharField(max_length=200)
    itemcolor = serializers.CharField(max_length=200)
    itemsize = serializers.CharField(max_length=200)
    stockinhand = serializers.CharField(max_length=200)
    stockinwarehouse = serializers.CharField(max_length=200) 
    uniquecode = serializers.CharField(max_length=200)


    class Meta:
        model = Items
        fields = ('__all__')