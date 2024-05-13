from django.contrib import admin
from django.urls import path
from displayApp import views

urlpatterns = [
    path('display/', views.display)
]