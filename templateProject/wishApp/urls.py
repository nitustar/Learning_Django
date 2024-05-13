from django.contrib import admin
from django.urls import path, include
from wishApp import views

urlpatterns = [
    path('greet/', views.hello),
]