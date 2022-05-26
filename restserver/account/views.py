from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
import logging
from spurusers.models import Spurusers
from spurusers.serializers import SpurusersSerializer


class LoginView(APIView):

    def post(self, request):
        try:
            user_var = Spurusers.objects.get(email=request.data["email"])
            serializer = SpurusersSerializer(user_var)
            dpassword = serializer.data['password']
            if request.data["password"] == dpassword:
                data = serializer.data
                return Response({"status": "success", "data": data, "msg": "True"})
            else:
                return Response({"status": "error", "msg": "Passwords do not match, try again"})
        except Spurusers.DoesNotExist:
            user = None
            return Response({"status": "error", "msg": "User Does not match, try again"})

