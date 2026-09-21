from django.db import models
from django.contrib.auth.models import User
class Rooms(models.Model):
 room_status=models.CharField(max_length=20,default="vacant")
 room_price=models.DecimalField(max_digits=10,decimal_places=2)
 room_number=models.IntegerField(unique=True)
 def __str__(self):
  return f"Room {self.room_number} -{self.room_status}"
class Tenant(models.Model):
  name=models.CharField(max_length=20)
  phone=models.CharField(max_length=10)
  room=models.ForeignKey(Rooms,on_delete=models.CASCADE)
 
# Create your models here.
 
