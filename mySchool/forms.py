from django import forms
from .models import Hostel,Room


class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ["name","location","description","phone_number","email"]

class RoomForm(forms.ModelForm):
    class Meta:
     model=Roomo
     fields = ["room_number","capacity"]
