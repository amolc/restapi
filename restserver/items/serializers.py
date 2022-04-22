from rest_framework import serializers
from .models import Items

class ItemsSerializer(serializers.ModelSerializer):
    org_id = serializers.FloatField()
    name = serializers.CharField(max_length=200)
    name =serializers.CharField(max_length=200)

    class Meta:
        model = Items
        fields = ('__all__')