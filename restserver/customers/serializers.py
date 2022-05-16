from rest_framework import serializers
from .models import Customers

class CustomersSerializer(serializers.ModelSerializer):
    org_id = serializers.FloatField()
    customer_id = serializers.FloatField()
    name = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)
    country = serializers.CharField(max_length=200)
    
    class Meta:
        model = Customers
        fields = ('__all__')