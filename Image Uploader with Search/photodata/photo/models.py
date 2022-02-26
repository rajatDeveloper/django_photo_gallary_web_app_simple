from tkinter import CASCADE
from tokenize import blank_re
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    title = models.CharField(max_length=40 , default="Title_user")
    image = models.ImageField(null=False ,blank = False)

    def __str__(self):
        return self.title      