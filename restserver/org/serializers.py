from rest_framework import serializers
from .models import Org

class OrgSerializer(serializers.ModelSerializer):
    org_name = serializers.CharField(max_length=200)
    org_address = serializers.CharField(max_length=200)
    org_telephone = serializers.FloatField()
    org_zip = serializers.FloatField()
    org_email = serializers.CharField(max_length=200)
    org_password = serializers.CharField(max_length=30)

    class Meta:
        model = Org
        fields = ('__all__')