from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=200, blank=True, null=True)
    zip = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.PositiveIntegerField()
    email = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=54, default='')

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name
