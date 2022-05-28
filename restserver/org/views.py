from django.shortcuts import render
from django.shortcuts import get_object_or_404
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrgSerializer
from .models import Org


class OrgViews(APIView):
    def post(self, request):
        logging.warning(request.data)
        serializer = OrgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Org.objects.get(id=id)
            serializer = OrgSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Org.objects.all()
        serializer = OrgSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        id = request.data.get("id")
        item = Org.objects.get(id=id)
        serializer = OrgSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(Org, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class OrgLoginView(APIView):

    def post(self, request):
        try:
            user_var = Org.objects.get(email=request.data["email"])
            serializer = OrgSerializer(user_var)
            dpassword = serializer.data['password']
            if request.data["password"] == dpassword:
                data = serializer.data
                return Response({"status": "success", "data": data, "msg": "True"})
            else:
                return Response({"status": "error", "msg": "Passwords do not match, try again"})
        except Org.DoesNotExist:
            user = None
            return Response({"status": "error", "msg": "User Does not match, try again"})
