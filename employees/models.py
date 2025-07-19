from django.db import models

# Create your models here.



# **it conatins the essential field and the behavior of the 
# **data your storing in the database
# **infact we create database fields by writing the models classes in this files
# **we work more ofen in this files
# 
#  

# **To create a table first create a class
class Employee(models.Model):
    # **these are fields of the table
    frist_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/')
    designation=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    # **unique=True is used to make sure that the email is unique
    phone_number=models.CharField(max_length=12,blank=True)
    # **blank=True is used to make the field optional
    created_at=models.DateTimeField(auto_now_add=True)
    # **auto_now_add=True is used to set the current date and time when the object is created
    updated_at=models.DateTimeField(auto_now=True)
    # **auto_now=True is used to set the current date and time when the object is updated







