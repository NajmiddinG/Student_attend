from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='users/%Y-%m-%d/', default='users/profil.png')


class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    nomer = models.CharField(max_length=20)
    message = models.TextField(max_length=500)


class Student(models.Model):
    roll_no = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    sem = models.IntegerField(default=1)
    branch = models.CharField(max_length=40)
    gender = models.CharField(max_length=6, default='Male')
    nomer = models.IntegerField()
    email = models.EmailField(max_length=40)
    city = models.CharField(max_length=40)
    pincode = models.IntegerField()
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.first_name


class StudentAttend(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    atten_date = models.DateField()
    in_time = models.TimeField()
    out_time = models.TimeField()
    description = models.CharField(max_length=250)
