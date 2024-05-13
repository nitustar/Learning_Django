from django.shortcuts import render
import datetime

# Create your views here.

def hello(request):
    time = datetime.datetime.now()
    if time.strftime("%H") < '12' and time.strftime("%H") > '00' :
        greet = "Morning"
    elif time.strftime("%H") > '12' and time.strftime("%H") < '16' :
        greet = "Afternoon"
    else :
        greet = "Evening"
    print(time)
    my_dict = {'greet':greet}
    return render(request, 'wishApp/greeting.html', context=my_dict)

# time = datetime.datetime.now().time()
# # if time < '12.00AM'
# print(time.strftime("%H:%M:%S"))