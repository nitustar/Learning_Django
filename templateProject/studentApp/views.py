from django.shortcuts import render
import datetime

# Create your views here.

def student(request):
    name = "Nitesh"
    age = "26"
    std = 10
    rollno = 101
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    my_dict = {'name':name, 'class':std, 'roll':rollno, 'age':age, 'date':date, 'time':time}
    return render(request, 'studentApp/student.html', context=my_dict)
