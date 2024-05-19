from django.shortcuts import render, redirect
from .models import Sign_up
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def error(request):
    return render(request, '404_error.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def tc(request):
    return render(request, 'tc.html')

def room(request):
    return render(request, 'rooms.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        Phone_Number = request.POST['Phone_Number']
        email= request.POST['email']
        password= request.POST['password']
        Confirm_password= request.POST['Confirm_password']

        if Sign_up.objects.filter(username = username).exists():
            messages.error(request,'Username already taken')
            return redirect(signup)
        
        if password != Confirm_password:
            messages.error(request,'Password does not match')
            return redirect(signup)


        Data = Sign_up(name=name, username=username, Phone_Number=Phone_Number, email=email, password=password, 
                       Confirm_password=Confirm_password)
        Data.save()
    return render(request, 'sign_up.html')

def forgot(request):
    return render(request, 'forgot.html')

def set_password(request):
    return render(request, 'set_password.html')
    