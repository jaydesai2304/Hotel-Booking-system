from django.contrib import admin
from .models import Sign_up, Contact

class register(admin.ModelAdmin):
    list_display = ("name","username","Phone_Number","email","password")
    
admin.site.register(Sign_up, register)

class contact_details(admin.ModelAdmin):
    list_display = ("name","phone_no","email", "message")

admin.site.register(Contact, contact_details)