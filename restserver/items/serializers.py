from rest_framework import serializers
from .models import Items

class ItemsSerializer(serializers.ModelSerializer):
    org_id = serializers.FloatField()
    item_name =serializers.CharField(max_length=200)
    item_description = serializers.CharField(max_length=200)
    item_price = serializers.CharField(max_length=200)
    item_picture = serializers.CharField(max_length=200)
    item_longtext = serializers.CharField(max_length=200)
    item_stock = serializers.CharField(max_length=200)

    class Meta:
        model = Items
        fields = ('__all__')