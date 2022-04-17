from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    org_id = serializers.FloatField()
    name = serializers.CharField(max_length=200)
    name =serializers.CharField(max_length=200)

    class Meta:
        model = Category
        fields = ('__all__')