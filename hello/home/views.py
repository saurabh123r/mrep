from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from home.models import Contact
from django import *


# Create your views here.


def index(request):
    return render(request, 'index.html')


def addmission(request):
    return render(request, 'addmission.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc)
        contact.save()
        messages.success(request, 'Your massege has been sent!')
    return render(request, 'contact.html')


#  Authentication code started here
def signout(request):
    logout(request)
    return redirect('/')


def signup(request):
    pass
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()
        messages.success(request, "your Account Has been created")
        return redirect('/signin')

    return render(request, "signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            firstname = user.first_name
            messages.success(request, "You are succesfully logged In")
            return redirect('/', firstname)
        else:
            return render(request, 'signin.html')

    return render(request, "signin.html")
# Authentication code ended here
