from django.shortcuts import render
from django.shortcuts import get_object_or_404
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student


class StudentViews(APIView):
    def post(self, request):
        logging.warning(request.data)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        id = request.data.get("id")
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        student = get_object_or_404(Student, id=id)
        student.delete()
        return Response({"status": "success", "data": "Item Deleted"})
