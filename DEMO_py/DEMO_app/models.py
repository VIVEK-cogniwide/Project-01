from django.db import models

# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    designation = models.CharField(max_length=50)
    salary = models.CharField(max_length=10)