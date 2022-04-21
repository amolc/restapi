# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AppusersSerializer
from .models import Appusers

class AppusersViews(APIView):
    def post(self, request):
        serializer = AppusersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Appusers.objects.get(id=id)
            serializer = AppusersSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Appusers.objects.all()
        serializer = AppusersSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


    def patch(self, request, id=None):
        item = Appusers.objects.get(id=id)
        serializer = AppusersSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(Appusers, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})