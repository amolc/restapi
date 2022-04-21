from django.db import models

class Spurusers(models.Model):
    orgName = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    userPhone = models.CharField(max_length=200)
    demoOrgID = models.CharField(null=True, blank=True,max_length=200)
    demoOrgID = models.CharField(null=True, blank=True,max_length=200)
    demo_key = models.CharField(null=True, blank=True,max_length=200)
    demo_value = models.CharField(null=True, blank=True,max_length=200)
    liveOrgID = models.CharField(null=True, blank=True,max_length=200)
    live_key = models.CharField(null=True, blank=True,max_length=200)
    live_value = models.CharField(null=True, blank=True,max_length=200)
    liveOrgID = models.CharField(null=True, blank=True,max_length=200)
    paymentID = models.CharField(null=True, blank=True,max_length=200)
    notes = models.CharField(null=True, blank=True,max_length=200)