from django.db import models

class Org(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    telephone = models.PositiveIntegerField()
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=30)
    domain = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)



