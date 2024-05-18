from django.db import models

# Create your models here.

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=255)

    def __str__(self):
        return 'Employee Object with eno: +str(self.no)'
    

class Job(models.Model):
    posting_date = models.DateField()
    location = models.CharField(max_length=30)
    offered_salary = models.FloatField()
    qualification = models.CharField(max_length=30)


class Book(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    published_date = models.DateField()


class Customer(models.Model):
    name = models.CharField(max_length=30)
    ano = models.IntegerField()
    mail_id = models.EmailField(max_length=50)
    phone_number = models.IntegerField()
    age = models.IntegerField()