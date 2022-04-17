from django.db import models

class Category(models.Model):
    org_id = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
