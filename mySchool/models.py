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

    ROLE_CHOICES = [("OWNER", "Owner"),("TENANT", "Tenant")]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES)
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

class Tenancy(models.Model):
 tenant=models.ForeignKey(UserProfile,on_delete=models.PROTECT,limit_choices_to={"role":"TENANT"},related_name="tenancies")
 room = models.ForeignKey(Room,on_delete=models.PROTECT,related_name="tenancies")
 start_date = models.DateField(auto_now_add=True)
 end_date = models.DateField(null=True, blank=True)
 is_active = models.BooleanField(default=True)
 class Meta:
  constraints = [models.UniqueConstraint(fields=["tenant"],condition=models.Q(is_active=True),name="unique_active_tenancy_per_tenant")]
 def __str__(self):
  return f"{self.tenant.user.username} - {self.room}"

 def clean(self):
  from django.core.exceptions import ValidationError
  if not self.is_active:
   return
  # A tenant must have the TENANT role.
  if self.tenant.role != "TENANT":
   raise ValidationError({"tenant": "Only users with the TENANT role can be assigned to a room."})
  # Check whether this tenant already has another active tenancy.
   existing_tenancy = Tenancy.objects.filter(tenant=self.tenant,is_active=True).exclude(pk=self.pk)
   if existing_tenancy.exists():
    raise ValidationError({"tenant": "This tenant already has an active room assignment."})
    # Count other active tenants assigned to this room.
    active_tenants = Tenancy.objects.filter(room=self.room,is_active=True).exclude(pk=self.pk).count()
   if active_tenants >= self.room.capacity:
    raise ValidationError({"room": "This room has reached its capacity."})     
