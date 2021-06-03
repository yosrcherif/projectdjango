from django.db import models
from datetime import datetime
from django.db.models.base import Model

from django.db.models.fields import CharField
# Create your models here.
class UserDetails(models.Model):
    name = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

class todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    descr = models.TextField(blank=True)
    cmpte = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now())

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now())
    details = models.OneToOneField(UserDetails,on_delete=models.CASCADE)
    todolist = models.ManyToManyField(todo,blank=False,null = True)





