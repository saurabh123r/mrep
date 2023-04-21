from django.contrib import admin
from django.urls import path
from home import views


# Url for our LWS
urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('addmission', views.addmission, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('signin', views.signin, name='SignIn'),
    path('signup', views.signup, name='SignUp'),
    path('signout', views.signout, name='SignOut'),
]


# Admin panel customization

admin.site.site_header = "LearnWithSaurya"
admin.site.site_title = "Learn To Hyper - LearnWithSaurya"
admin.site.index_title = "Welcome to LWS"
