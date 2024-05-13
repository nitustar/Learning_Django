from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def welcome_view(request):
    return HttpResponse("<h2>Welcome to Django Project!!</h2>")

def time_view(request) :
    time = datetime.datetime.now()
    s = "<h2>Todays Date and Time is "+str(time)+"</h2>"
    return HttpResponse(s)