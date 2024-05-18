from django.urls import path  
from hotel import views 

urlpatterns = [   
    path('', views.index,name="index"),
    path('error/',views.error, name="error"),
    path('about/',views.about, name="about"),
    path('service/',views.service, name="service"),
    path('contact/',views.contact, name="contact"),
    path('tc/',views.tc, name="tc"),
    path('room/',views.room, name="room"),
    path('login/',views.login, name="login"),
    path('signup/',views.signup, name="signup"),
    path('forgot/',views.forgot, name="forgot"),
    

]   