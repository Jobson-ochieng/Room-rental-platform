from django import forms
from .models import Hostel,Room,Tenancy,UserProfile


class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ["name","location","description","phone_number","email"]

class RoomForm(forms.ModelForm):
    class Meta:
     model=Room
     fields = ["room_number","capacity"]

class TenancyForm(forms.ModelForm):
    tenant = forms.ModelChoiceField(queryset=UserProfile.objects.filter(role="TENANT"),label="Select Tenant")
    class Meta:
        model = Tenancy
        fields = ["tenant"]
