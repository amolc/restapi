from django.db import models

class Customers(models.Model):
    org_id = models.PositiveIntegerField()
    customer_id = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    
