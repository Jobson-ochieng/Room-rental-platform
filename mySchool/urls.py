from django.contrib import admin
from django.urls import path
from . import views 
from django.contrib.auth import views as auth
urlpatterns = [
    path('reg/',views.reg,name='registration'),
    path('login/',auth.LoginView.as_view(template_name='html/login.html'),name='sign_in'),
    path('logout/',auth.LogoutView.as_view(),name='logout'),
    path('book/',views.book,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
]
