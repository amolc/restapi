from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    users_name = serializers.CharField(max_length=200)
    users_address = serializers.CharField(max_length=200)
    users_telephone = serializers.FloatField()
    users_zip = serializers.FloatField()
    users_email = serializers.CharField(max_length=200)
    users_password =serializers.CharField(max_length=200)

    class Meta:
        model = Users
        fields = ('__all__')