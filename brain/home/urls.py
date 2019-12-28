from django.urls import path,include
from django.contrib import admin
from . import views
from django.contrib.auth import views as authentication_views


app_name = 'home'

urlpatterns = [

    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('otp/',views.otp,name='otp'),
    path('login/',authentication_views.LoginView.as_view(template_name='home/login.html'),name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='home/logout.html'),name='logout'),



]
