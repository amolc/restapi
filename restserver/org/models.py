from django.db import models

class Org(models.Model):
    org_name = models.CharField(max_length=200)
    org_address = models.CharField(max_length=200)
    org_telephone = models.PositiveIntegerField()
    org_zip = models.PositiveIntegerField()
    org_email = models.CharField(max_length=200)
    org_password = models.CharField(max_length=30)



