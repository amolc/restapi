# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrdersSerializer,OrderDetailsSerializer
from .models import Orders,OrderDetails

import stripe
import json
import logging 

class OrdersViews(APIView):
    def post(self, request):
        data = request.data
        data['name'] = data['billingname']
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            orderId = obj.id 
        else:
            print(serializer.errors)
        print(orderId)

        orders = Orders.objects.get(id=orderId)
        items = {}
        items['org_id'] = data['org_id']
        items['orderid'] = orderId
        items['itemname'] = data['name']
        items['itemqty'] = data['qty']
        items['itemcost'] = data['price']
        print(items)
        orderserializer = OrderDetailsSerializer(data=items)
        orderserializer.is_valid(raise_exception=True)
        if orderserializer.is_valid():
            obj = orderserializer.save()
            logging.warning("order details saved successfully")
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            logging.warning(serializer.errors)
            logging.warning("there is an error")
            return Response({"status": "error", "data": serializer.errors})
       


    def get(self, request, id=None):
        if id:
            item = Orders.objects.get(id=id)
            serializer = OrdersSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Orders.objects.all().order_by('-id')
        serializer = OrdersSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


    def patch(self, request, id=None):
        item = Orders.objects.get(id=id)
        serializer = OrdersSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(Orders, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})



class StripeChargeViews(APIView):
    def post(self, request):
        data=request.data
        logging.warning(data)

        stripe.api_key = "sk_test_51GafYFIYdfL0AKdDOHfaXpB68RVHdvNdsjfIHwCGN9QvOXpji3IwM8EQ7oTzC5ksrJaY8rUUKip1FtCM0zONsnhF00aZASVpfs"

        amount =  data['amount'] 
        amount = int(amount)*100 

        response = stripe.Charge.create(
                        amount=amount,
                        currency="sgd",
                        source= data['token'] ,
                        description="My First Test Charge (created for API docs at https://www.stripe.com/docs/api)",
                        )


        # response.id payment id 
    
        orderId = data['orderId']
        logging.warning(orderId)

        items = {}
        items['paymentId'] = response.id
        items['setstatus'] = "In Progress"
        print(items)

        item = Orders.objects.get(id=orderId)
        serializer = OrdersSerializer(item, data=items, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


class OrderDetailsViews(APIView):
    logging.warning("order details page")
    def post(self, request):
        data = request.data 
        orderid = data['orderid']
        logging.warning(orderid)
        item = OrderDetails.objects.get(orderid=orderid)
        serializer = OrderDetailsSerializer(item)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

       