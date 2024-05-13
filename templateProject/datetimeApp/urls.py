from django.contrib import admin
from django.urls import path
from datetimeApp import views

urlpatterns = [
    path("datetime/", views.datetime),
]