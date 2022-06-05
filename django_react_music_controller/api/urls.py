"""api.urls URL Configuration
"""
from django.urls import path
from .views import main

urlpatterns = [
    path('', main) # blank URL calls "main"
]
