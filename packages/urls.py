from django.urls import path
from .views import *

urlpatterns = [
    path('', PackageListView.as_view(), name='product-list'),
    # Add more URL patterns as needed for other views
]