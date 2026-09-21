from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import TenantForm
from .models import Tenant
def dashboard(request):
 lists=Tenant.objects.all()
 return render(request,'html/list.html',{'lists':lists})
def book(request):
 if request.method=='POST':
  form=TenantForm(request.POST)
  if form.is_valid():
   tenant=form.save(commit=False)
   tenant.user=request.user
   tenant.save()
   return redirect('dashboard')
 else:
  form=TenantForm()
 return render(request,'reg/data.html',{'form':form})
def reg(request):
 if request.method=='POST':
  form=UserCreationForm(request.POST)
  if form.is_valid():
   form.save()
   return redirect('login')
 else:
  form=UserCreationForm()
 return render(request,'reg/reg.html',{'form':form})
# Create your views here.
