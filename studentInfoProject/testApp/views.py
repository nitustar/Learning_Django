from django.shortcuts import render
from testApp.models import Student

# Create your views here.

# def studentview(request):
#     # student_list = Student.objects.order_by('marks')
#     # my_dict = {'student_list':student_list}
#     return render(request, 'testApp/student.html', context=my_dict)

def home_page_view(request):
    students = Student.objects.all()
    #students=Student.objects.filter(marks__lt=35) 
    #students=Student.objects.filter(name__startswith='A') 
    #students=Student.objects.all().order_by('marks') 
    #students=Student.objects.all().order_by('-marks')
    return render(request, 'testApp/index.html', {'students':students})
