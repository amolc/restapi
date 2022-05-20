from django.db import models

class Orders(models.Model):
    org_id = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    postalcode = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    paymentId = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    setstatus = models.CharField(max_length=200)

class OrderDetails(models.Model):
    org_id = models.PositiveIntegerField()
    orderid = models.PositiveIntegerField()
    itemname = models.CharField(max_length = 100)
    itemqty = models.CharField(max_length = 100)
    itemcost = models.CharField(max_length = 100)
    itemcolor = models.CharField(max_length = 100,default=None, blank=True, null=True)
    itemsize = models.CharField(max_length = 100,default=None, blank=True, null=True)
   
    
   
    
