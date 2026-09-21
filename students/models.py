from django.db import models
from django.contrib.auth.models import User
class Students(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='students')
   age=models.IntegerField()
   name=models.CharField(max_length=100)
   course=models.CharField(max_length=100)

   def __str__(self):
    return self.name 
# Create your models here.
