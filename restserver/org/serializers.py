from rest_framework import serializers
from .models import Org

class OrgSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)
    company = serializers.CharField(max_length=30)
    address = serializers.CharField(max_length=50)
    address2 = serializers.CharField(max_length=50)
    zip = serializers.CharField()
    country = serializers.CharField(max_length=20)
    telephone = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)
    domain = serializers.CharField(max_length=30)
    slug = serializers.CharField(max_length=30)

    class Meta:
        model = Org
        fields = ('__all__')