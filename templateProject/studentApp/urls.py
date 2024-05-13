from django.contrib import admin
from django.urls import path, include
from studentApp import views

urlpatterns=[
    path('student/',views.student),
]