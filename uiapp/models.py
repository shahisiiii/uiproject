from django.db import models

# Create your models here.


class RegisterModel(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    
