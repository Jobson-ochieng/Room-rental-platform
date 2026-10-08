from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hostel(models.Model):
 owner=models.ForeignKey(User,on_delete=models.CASCADE)
 name=models.CharField(max_length=100)
 location=models.CharField(max_length=200)
 description = models.TextField(blank=True)
 phone_number = models.CharField(max_length=20, blank=True)
 email = models.EmailField(blank=True)
 is_active = models.BooleanField(default=True)
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)

 class Meta:
    ordering = ["-created_at"]
 def __str__(self):
  return self.name

class UserProfile(models.Model):

    ROLE_CHOICES = [
        ("OWNER", "Owner"),
        ("TENANT", "Tenant"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )
    def __str__(self):
        return f"{self.user.username} - {self.role}" 

class Room(models.Model):
    hostel = models.ForeignKey(Hostel,on_delete=models.CASCADE)
    room_number = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField()
    is_occupied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
     return f"{self.hostel.name} - Room {self.room_number}"
    class Meta:
       constraints = [
        models.UniqueConstraint(
            fields=["hostel", "room_number"],
            name="unique_room_number_per_hostel",
          )
      ]
