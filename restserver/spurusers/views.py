# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status
from rest_framework import mixins
from .serializers import SpurusersSerializer
from .models import Spurusers
import random 
import logging


class SpurusersViews(APIView):
    def post(self, request):

        serializer = SpurusersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors})

    def get(self, request, id=None):
        if id:
            item = Spurusers.objects.get(id=id)
            serializer = SpurusersSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Spurusers.objects.all()
        serializer = SpurusersSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


    def patch(self, request, id=None):
        item = Spurusers.objects.get(id=id)
        serializer = SpurusersSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(Spurusers, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class SpurusersUserViews(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    @action(methods=['post'], detail=False)    
    def login(self, request):
        email = request.data['email']
        password = request.data['password']
        logging.warning(email) 
        logging.warning(password) 
        id=6
        item = Spurusers.objects.get(id=id)
        serializer = SpurusersSerializer(item)
        dpassword = serializer.data['password']
        logging.warning(serializer.data['password']) 
        if(password == dpassword ):
            data = serializer.data
            return Response({"status": "success", "data": "Login Called"})
        else :
            return Response({"status": "error", "data": "User Does not match, try again"})

    
    @action(methods=['post'], detail=False)    
    def register(self, request):
        # email = request.data['email']
        # password = request.data['password']
        logging.warning(request.data) 

        # if request.data['password'] != request.data['confirmpassword']:
        #     return Response({"status": "issue", "msg": "Password do not match"})

        # else :
        data = request.data

        name = data['name']
        email = request.data['email']
        password = request.data['password']
        orgName = data['orgName']
        phone = request.data['phone']
        usertype = request.data['usertype']
        

        # Lets create the remaining fields of the database 

        # orgName = models.CharField(max_length=200)
        # name = models.CharField(max_length=200)
        # email = models.CharField(max_length=200)
        # password = models.CharField(max_length=200)
        # userPhone = models.CharField(max_length=200)
        # usertype = models.CharField(null=True, blank=True,max_length=200)

        value = random.randint(5252,6252)
        value1 = random.randint(6252,7252)
        value3 = random.randint(1252,3252)

        value = str(value)
        value1 = str(value1)
        value3 = str(value3)

        orgkey = orgName.replace(".", "")
        orgkey = orgkey.replace(",", "")
        orgkey = orgkey.replace(" ", "")
        if len(orgkey) > 10 : 
            orgkey = orgkey[0:10]
            orgkey = orgkey.upper()
            demoorgkey = value+orgkey+"DEMO"+value1
            liveorgkey = value+orgkey+"LIVE"+value3

        else : 
            orgkey = orgkey.upper()
            demoorgkey = value+orgkey+"DEMO"+value1
            liveorgkey = value+orgkey+"DEMO"+value3

    
        demosecret =  ''.join(random.SystemRandom().choice(orgkey + value1) for _ in range(32))
        livesecret =  ''.join(random.SystemRandom().choice(orgkey + value1) for _ in range(32))
        
        logging.warning(demoorgkey) 
        logging.warning(demosecret) 
        logging.warning("       ") 
        logging.warning(liveorgkey) 
        logging.warning(livesecret) 

        data['demo_key'] = demoorgkey
        data['demo_value'] = demosecret
        data['live_key'] = liveorgkey
        data['live_value'] = livesecret

        

        serializer = SpurusersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response({"status": "success", "data": serializer.data,"msg": "user successfully added"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors})


       
      