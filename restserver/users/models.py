from django.db import models

class Users(models.Model):
    users_name = models.CharField(max_length=200)
    users_address = models.CharField(max_length=200)
    users_telephone = models.PositiveIntegerField()
    users_zip = models.PositiveIntegerField()
    users_email = models.CharField(max_length=200)
    users_password = models.CharField(max_length=30)
