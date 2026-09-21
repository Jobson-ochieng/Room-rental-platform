"""
URL configuration for Jobson project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path,include
from students import views
urlpatterns = [
    path('',views.home),
    path('',include('mySchool.urls')),
    path('admin/', admin.site.urls),
    path('about/',views.about),
    path('students/',views.students_list,name='students_list'),
    path('students/add/',views.students_create,name='students_create'),
    path('students/<int:id>/edit/',views.student_update,name='student_update'),
    path('students/<int:id>/delete/',views.students_delete,name='students_delete'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('register/',views.register,name='register'),
    path('hello/',views.HelloView.as_view())
]
