# userapp/admin.py
from django.contrib import admin
from .models import Package

admin.site.register(Package)
