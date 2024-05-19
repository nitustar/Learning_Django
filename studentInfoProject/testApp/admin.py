from django.contrib import admin
from testApp.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=["rollno","name", "dob", "marks", "email", "phonenumber", "address"]

admin.site.register(Student, StudentAdmin)