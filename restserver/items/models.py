from django.db import models

class Items(models.Model):
    org_id = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    thumbnail = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    longtext = models.CharField(max_length=200)
    itemcolor = models.CharField(max_length=200)
    itemsize = models.CharField(max_length=200)
    stockinhand = models.CharField(max_length=200)
    stockinwarehouse = models.CharField(max_length=200)
    uniquecode = models.CharField(max_length=200)
    
   


    
