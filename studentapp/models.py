from django.db import models
from datetime import datetime 
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image =             models.ImageField(upload_to='users/%Y-%m-%d/', default='users/profil.png')



class ContactInfo(models.Model):
    name =              models.CharField(max_length=100)
    email =             models.EmailField(max_length=100)
    nomer =             models.CharField(max_length=20)
    message =           models.TextField(max_length=500)

class Student(models.Model):
    roll_no =           models.CharField(max_length=40)
    first_name =        models.CharField(max_length=40)
    last_name =         models.CharField(max_length=40)
    sem =               models.IntegerField(default=1)
    branch =            models.CharField(max_length=40)
    gender =            models.CharField(max_length=6, default='Male')
    nomer =             models.IntegerField()
    email =             models.EmailField(max_length=40)
    city =              models.CharField(max_length=40)
    pincode =           models.IntegerField()
    address =           models.TextField(max_length=200)

class StudentAttend(models.Model):
    student =           models.ForeignKey(Student, on_delete=models.CASCADE)
    atten_date =        models.DateField()
    in_time =           models.DateTimeField()
    out_time =          models.DateTimeField()
    description =       models.CharField(max_length=150)