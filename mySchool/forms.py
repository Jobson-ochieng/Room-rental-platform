from .models import Tenant
from django import forms
class TenantForm(forms.ModelForm):
 class Meta:
  model=Tenant
  fields=["phone","name","room"]

