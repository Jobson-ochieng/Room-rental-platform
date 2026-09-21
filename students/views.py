from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Students
from .forms import StudentsForm
from django.views import View
def home(request):
 context={
   "name":"Jobson",
   }
 return render(request,'home.html',context)
def about(request):
    return HttpResponse("This is the about page.")
@login_required	
def students_list(request):
   students = Students.objects.filter(user=request.user)
   return render(request,'students/students_list.html',{
'students':students
}
)
def students_create(request):
 if request.method=='POST':
  form=StudentsForm(request.POST)
  if form.is_valid():
   students= form.save(commit=False)
   students.user=request.user
   students.save()
   return redirect('students_list')
 else:
  form=StudentsForm()
 return render(request,'students/students_form.html',{
 'form':form
}
)   

def student_update(request,id):
 student=get_object_or_404(Students,id=id,user=request.user)
 if request.method=='POST':
  form=StudentsForm(request.POST,instance=student) 
  if form.is_valid():
   form.save()
   return redirect('students_list')
 else:
   form=StudentsForm(instance=student)
 return render(request,'students/students_form.html',{
 'form':form
  }
)
def students_delete(request,id):
 student=get_object_or_404(Students,id=id,user=request.user)
 if request.method=='POST':
  student.delete()
  return redirect('students_list')
 return render(request,'students/students_confirmation_list.html',{'students':student})
def register(request):
 if request.method=='POST':
  form=UserCreationForm(request.POST)
  if form.is_valid():
   form.save()
   return redirect('login')
 else:
  form=UserCreationForm()
 return render(request,'registration/register.html',{'form':form})
class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello from a class-based view!")
    def post(self, request):
        return HttpResponse("This is a POST request")
# Create your views here.
