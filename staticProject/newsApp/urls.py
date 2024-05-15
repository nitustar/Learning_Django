from django.contrib import admin
from django.urls import path
from newsApp import views

urlpatterns = [
    path("wish/", views.wish),
]