from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('/<productName>', views.home, name='product'),
    path('allProducts', views.allProducts, name='allProducts'),
]
