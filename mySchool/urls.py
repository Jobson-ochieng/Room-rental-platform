from django.contrib import admin
from django.urls import path
from . import views 
from django.contrib.auth import views as auth
urlpatterns = [
    path('reg/',views.reg,name='registration'),
    path('login/',auth.LoginView.as_view(template_name='login.html'),name='sign_in'),
    path('logout/',auth.LogoutView.as_view(),name='logout'),
    path('create_hostel/', views.create_hostel, name='create_hostel'),    
    path('dashboard/', views.dashboard, name='dashboard'),
    path( 'create_room/<int:hostel_id>/rooms/create/',views.create_room,name='create_room'),
    path('rooms/<int:room_id>/edit/',views.edit_room,name='edit_room'),
    path('rooms/<int:room_id>/assign-tenant/',views.assign_tenant,name='assign_tenant'),
    path('tenancies/<int:tenancy_id>/end/',views.end_tenancy,name='end_tenancy'),
]
