from django.db import models

# Create your models here.
class courses(models.Model):
    course_title = models.CharField(max_length=100)
    course_dec = models.TextField(max_length=200)
    course_duration = models.CharField(max_length=20)

class workshop(models.Model):
    workshop_title = models.CharField(max_length=100)
    workshop_dec = models.TextField(max_length=200)
    workshop_duration = models.CharField(max_length=20)

class contacts(models.Model):
    studentname = models.CharField(max_length=20)
    studentemail = models.EmailField()
    coursename = models.CharField(max_length=50)
    mobileno = models.IntegerField()
    massage = models.TextField(max_length=100)
    
