"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    #path('appName/',include('appName.urls')),
    path('polls/',include('polls.urls')),
    path('admin/', admin.site.urls),
]
