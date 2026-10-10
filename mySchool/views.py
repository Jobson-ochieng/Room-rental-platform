from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Count, Q

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import HostelForm,RoomForm,TenancyForm,Tenancy
from .models import Hostel,UserProfile,Room
from django.core.exceptions import ValidationError

@login_required
def dashboard(request):
 hostels = Hostel.objects.all().prefetch_related("room_set__tenancies")
 for hostel in hostels:
  for room in hostel.room_set.all():
   room.active_tenant_count = room.tenancies.filter(is_active=True).count()
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

@login_required
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

@login_required
def create_room(request, hostel_id):
 hostel = get_object_or_404(Hostel,id=hostel_id,owner=request.user)
 if request.method=='POST':
  form=RoomForm(request.POST)
  if form.is_valid():
    room = form.save(commit=False)
    room.hostel = hostel
    room.save()
    return redirect('dashboard')
 else:
  form=RoomForm()
 return render(request,"create_room.html",{"form": form,"hostel": hostel})

@login_required
def edit_room(request,room_id):
 room = get_object_or_404(Room,id=room_id,hostel__owner=request.user)
 if request.method == 'POST':
  form = RoomForm(request.POST, instance=room)
  if form.is_valid():
   form.save()
   return redirect('dashboard')
 else:
  form = RoomForm(instance=room)
 return render(request,"edit_room.html",{"form": form,"room": room})

@login_required
def assign_tenant(request, room_id):
    room = get_object_or_404(Room,id=room_id,hostel__owner=request.user)

    if request.user.userprofile.role != "OWNER":
        return redirect("dashboard")

    if request.method == "POST":
        form = TenancyForm(request.POST)

        if form.is_valid():
            tenancy = form.save(commit=False)
            tenancy.room = room

            try:
                tenancy.full_clean()
                tenancy.save()
                return redirect("dashboard")
            except ValidationError as error:
                form.add_error(None, error)

    else:
        form = TenancyForm()

    return render(
        request,
        "assign_tenant.html",
        {
            "form": form,
            "room": room,
        },
    )

@login_required
def end_tenancy(request, tenancy_id):
    tenancy = get_object_or_404(Tenancy,id=tenancy_id,room__hostel__owner=request.user,is_active=True)

    is_owner = UserProfile.objects.filter(user=request.user,role="OWNER").exists()

    if not is_owner:
        return redirect("dashboard")

    if request.method == "POST":
        tenancy.is_active = False
        tenancy.end_date = timezone.localdate()
        tenancy.save(update_fields=["is_active", "end_date"])

    return redirect("dashboard")
