from django.conf.urls import url
from django.contrib import admin
from . import views 
from django.contrib.auth.views import LogoutView
urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^register/guest/$', views.guest_register_page, name='guestRegister'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
]
