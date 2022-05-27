# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemsSerializer
from .models import Items

class ItemsViews(APIView):
    def post(self, request):
        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,org_id=None,id=None):
        if id:
            item = Items.objects.get(id=id)
            serializer = ItemsSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Items.objects.filter(org_id=org_id)
        serializer = ItemsSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


    def patch(self, request, id=None):
        id = request.data.get('id')
        item = Items.objects.get(id=id)
        serializer = ItemsSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(Items, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class ListItemsViews(APIView):
    def get(self,request,org_id=None):
        items = Items.objects.filter(org_id=org_id)
        serializer = ItemsSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


    