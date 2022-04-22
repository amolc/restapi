from django.db import models

class Items(models.Model):
    org_id = models.PositiveIntegerField()
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.CharField(max_length=200)
    item_picture = models.CharField(max_length=200)
    item_longtext = models.CharField(max_length=200)
    item_stock = models.CharField(max_length=200)


    
