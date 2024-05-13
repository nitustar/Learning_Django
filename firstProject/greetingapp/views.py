from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def morning_view(request):
    s = "<h1>Hello, Good Morning!!</h1>"
    return HttpResponse(s)

def afternoon_view(request) :
    s = "<h1>Hello, Good Afternoon!!</h1>"
    return HttpResponse(s)

def evening_view(request) :
    s = "<h1>Hello, Good Evening!!</h1>"
    return HttpResponse(s)