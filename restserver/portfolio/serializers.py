from rest_framework import serializers
from .models import Portfolio

class PortfolioSerializer(serializers.ModelSerializer):
    org_id = serializers.FloatField()
    name = serializers.CharField(max_length=200)
    name =serializers.CharField(max_length=200)

    class Meta:
        model = Portfolio
        fields = ('__all__')