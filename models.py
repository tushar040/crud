from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms



class Todo(models.Model):
    task = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.task

class Category(models.Model):
    Category_Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    catimage = models.ImageField(upload_to ='uploads/')
    Action = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.Category_Name

class updatecat(models.Model):
    Category_Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    catimage = models.ImageField(upload_to='uploads/')

class Product(models.Model):
    Product_Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Product_Price = models.IntegerField(blank=True, null=True)
    Product_Quantity = models.IntegerField(blank=True, null=True)
    Product_Image = models.ImageField(upload_to ='uploads/')


    def __str__(self):
        return self.Product_Name

class EmployeeDetails(models.Model):
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    Gender = models.CharField(max_length=200)
    Ride = models.CharField(max_length=200)
    Emp_ID = models.CharField(max_length=200)
    Des = models.CharField(max_length=200)
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.f_name

COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)
class Student(models.Model):
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    mobile = models.IntegerField(blank=True, null=True)
    ride = models.CharField(max_length=200)
    mobile1 = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')

    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.f_name

class studentform(models.Model):
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.f_name
