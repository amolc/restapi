from rest_framework import serializers
from .models import Spurusers

class SpurusersSerializer(serializers.ModelSerializer):
    orgName = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    userPhone = serializers.CharField(max_length=200)
    demoOrgID = serializers.CharField(max_length=200)
    demo_key = serializers.CharField(max_length=200)
    demo_value = serializers.CharField(max_length=200)
    liveOrgID = serializers.CharField(max_length=200)
    live_key = serializers.CharField(max_length=200)
    live_value = serializers.CharField(max_length=200)
    paymentID = serializers.CharField(max_length=200)
    notes = serializers.CharField(max_length=200)
    usertype = serializers.CharField(max_length=200)

    class Meta:
        model = Spurusers
        fields = ('__all__')