from django.shortcuts import render, redirect
from .models import Sign_up, Contact, News_letter
from django.contrib import messages


def index(request):
    if request.method == "POST":
        newsletter_email = request.POST['newsletter_email']

        data = News_letter(newsletter_email=newsletter_email)
        data.save()
    return render(request, 'index.html')

def error(request):
    return render(request, '404_error.html')

def about(request):
    if request.method == "POST":
        newsletter_email = request.POST['newsletter_email']

        data = News_letter(newsletter_email=newsletter_email)
        data.save()
    return render(request, 'about.html')

def service(request):
    if request.method == "POST":
        newsletter_email = request.POST['newsletter_email']

        data = News_letter(newsletter_email=newsletter_email)
        data.save()
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        try:
            newsletter_email = request.POST['newsletter_email']

            data = News_letter(newsletter_email=newsletter_email)
            data.save()
        except:
            name = request.POST['name']
            phone_no = request.POST['phone_no']
            email = request.POST['email']
            message = request.POST['message']

            data = Contact(name=name, phone_no=phone_no, email=email, message=message)
            data.save()

    return render(request, 'contact.html')

def tc(request):
    if request.method == "POST":
        newsletter_email = request.POST['newsletter_email']

        data = News_letter(newsletter_email=newsletter_email)
        data.save()
    return render(request, 'tc.html')

def room(request):
    if request.method == "POST":
        newsletter_email = request.POST['newsletter_email']

        data = News_letter(newsletter_email=newsletter_email)
        data.save()
    return render(request, 'rooms.html')

def login(request):
    if request.method == "POST":
        try:
            user = Sign_up.objects.get(
                username = request.POST['username'],
                password = request.POST['password'],
                )
            request.session['username'] = user.username
            return render(request, 'index.html')
        except:
            return render(request, 'login.html')
    else:
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
    
def single_room(request):
    if request.method == "POST":
        newsletter_email = request.POST['newsletter_email']

        data = News_letter(newsletter_email=newsletter_email)
        data.save()
    return render(request, 'single_room.html')

def booking(request):
    if request.method == "POST":
        newsletter_email = request.POST['newsletter_email']

        data = News_letter(newsletter_email=newsletter_email)
        data.save()
    return render(request, 'booking.html')

def payment(request):
    if request.method == "POST":
        newsletter_email = request.POST['newsletter_email']

        data = News_letter(newsletter_email=newsletter_email)
        data.save()
    return render(request, 'payment.html')

def thanku(request):
    return render(request, 'thanku.html')

def more_hotels(request):
    return render(request, 'more_hotels.html')

