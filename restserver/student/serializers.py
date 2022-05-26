from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)
    zip = serializers.CharField(max_length=200)
    country = serializers.CharField(max_length=200)
    telephone = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=54, default='')

    class Meta:
        model = Student
        fields = ('__all__')
