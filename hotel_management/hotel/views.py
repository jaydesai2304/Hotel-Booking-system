from django.shortcuts import render

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
