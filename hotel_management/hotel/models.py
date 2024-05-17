from django.db import models

class Sign_up(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default='')
    Phone_Number = models.IntegerField(default='')
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    Confirm_password = models.CharField(max_length=100)