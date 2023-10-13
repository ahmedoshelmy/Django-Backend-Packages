from django.db import models
from packages.models import *


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    packages = models.ManyToManyField(Package, related_name='users')
