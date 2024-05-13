from django.shortcuts import render
import datetime
# Create your views here.

def datetime(request):
    dt = datetime.datetime.now()
    my_dict = {'show_datetime':dt}
    return render(request,'datetimeApp/datetime.html',context=my_dict)
