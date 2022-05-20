from rest_framework import serializers
from .models import Orders, OrderDetails

class OrdersSerializer(serializers.ModelSerializer):
    org_id = serializers.FloatField()
    name = serializers.CharField(max_length=200)
    address =serializers.CharField(max_length=200)
    address2 =serializers.CharField(max_length=200)
    postalcode =serializers.CharField(max_length=200)
    city =serializers.CharField(max_length=200)
    country =serializers.CharField(max_length=200)
    paymentId =serializers.CharField(max_length=200)
    amount =serializers.CharField(max_length=200)
    date =serializers.CharField(max_length=200)
    setstatus = serializers.CharField(max_length=200)

    class Meta:
        model = Orders
        fields = ('__all__')


class OrderDetailsSerializer(serializers.ModelSerializer):
    org_id = serializers.FloatField()
    orderid = serializers.FloatField()
    itemname =serializers.CharField(max_length=200)
    itemqty =serializers.CharField(max_length=200)
    itemcost =serializers.CharField(max_length=200)
    itemcolor =serializers.CharField(max_length=200, required=False)
    itemsize =serializers.CharField(max_length=200, required=False)
  

    class Meta:
        model = OrderDetails
        fields = ('__all__')