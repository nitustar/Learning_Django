from django.shortcuts import render

# Create your views here.
from testApp.models import Student

def studentview(request):
    student_list = Student.objects.order_by('marks')
    my_dict = {'student_list':student_list}
    return render(request, 'testApp/student.html', context=my_dict)