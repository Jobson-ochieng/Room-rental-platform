from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import HostelForm
from .models import Hostel,UserProfile

@login_required
def dashboard(request):
 hostels = Hostel.objects.filter(owner=request.user)
 roles=UserProfile.objects.filter(user=request.user)
 return render(request, "dashboard.html", {"hostels":hostels,"roles":roles}) 
@login_required
def create_hostel(request):
 role = request.user.userprofile.role
 if role != "OWNER":
  return redirect("dashboard")

 if request.method=='POST':
  form=HostelForm(request.POST)
  if form.is_valid():
   hostel=form.save(commit=False)
   hostel.owner=request.user
   hostel.save()
   return redirect('dashboard')
 else:
  form=HostelForm()
 return render(request, "create_hostel.html", {"form": form})

def reg(request):
 if request.method =='POST':
  form=UserCreationForm(request.POST)
  if form.is_valid():
   user=form.save()
   UserProfile.objects.create(user=user,role='OWNER')   
   return redirect('sign_in')
 else:
  form=UserCreationForm()
 return render(request,'reg/reg.html',{'form':form})


