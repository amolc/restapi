from rest_framework import serializers
from .models import Spurusers

class SpurusersSerializer(serializers.ModelSerializer):
    orgName = serializers.CharField(max_length=200,required=False)
    name = serializers.CharField(max_length=200,required=False)
    email = serializers.CharField(max_length=200,required=False)
    password = serializers.CharField(max_length=200,required=False)
    userPhone = serializers.CharField(max_length=200,required=False)
    demoOrgID = serializers.CharField(max_length=200,required=False )
    demo_key = serializers.CharField(max_length=200,required=False)
    demo_value = serializers.CharField(max_length=200,required=False)
    liveOrgID = serializers.CharField(max_length=200,required=False)
    live_key = serializers.CharField(max_length=200,required=False)
    live_value = serializers.CharField(max_length=200,required=False)
    paymentID = serializers.CharField(max_length=200,required=False)
    notes = serializers.CharField(max_length=200,required=False)
    usertype = serializers.CharField(max_length=200,required=False)
    demo_budgetallocated = serializers.CharField(max_length=200,required=False)
    demo_budgetused = serializers.CharField(max_length=200,required=False)
    live_budgetallocated = serializers.CharField(max_length=200,required=False)
    live_budgetused = serializers.CharField(max_length=200,required=False)

    class Meta:
        model = Spurusers
        fields = ('__all__')