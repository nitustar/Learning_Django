from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    rollno = models.IntegerField()
    dob = models.DateField()
    marks = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()
    phonenumber = models.IntegerField()
