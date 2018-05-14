
from django.db import models
# admin username: django pwd: admin123
# Create your models here.
from django.utils import timezone

class Account(models.Model):
    username  = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username




