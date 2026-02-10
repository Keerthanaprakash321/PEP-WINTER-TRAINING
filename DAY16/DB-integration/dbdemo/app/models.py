from django.db import models

# Create your models here.

class Driver(models.Model):

    name = models.TextField()

    license = models.TextField()

class Car(models.Model):

    make = models.TextField()

    model = models.TextField()

    year = models.IntegerField()

    owner = models.ForeignKey("Driver", on_delete=models.SET_NULL, null=True)
    
from django.db import models
class student(models.Model):
    stu_name = models.TextField()
    enr_num = models.TextField()
    course = models.TextField()
    sem = models.TextField()
    section = models.TextField()

class personal(models.Model):
    enr_num = models.ForeignKey("student", on_delete=models.SET_NULL, null=True)
    stu_name = models.TextField()
    mothers_name = models.TextField()
    fathers_name = models.TextField()
    add = models.TextField()
    ph_no = models.TextField()
    email = models.TextField()

    
    
