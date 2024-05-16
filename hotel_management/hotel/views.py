from django.shortcuts import render
from .models import Sign_up

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
        Phone_Number = request.POST['Phone_Number']
        email= request.POST['email']
        password= request.POST['password']
        Confirm_password= request.POST['Confirm_password']

        Data = Sign_up(name=name, Phone_Number=Phone_Number, email=email, password=password, Confirm_password=Confirm_password)
        Data.save()
    return render(request, 'sign_up.html')