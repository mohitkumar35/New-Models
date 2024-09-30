from django.db import models

# Create your models here.

class student(models.Model):
    stu_name=models.CharField(max_length=100)
    stu_email=models.EmailField()
    stu_password=models.CharField(max_length=50)
    stu_contact=models.IntegerField()
    