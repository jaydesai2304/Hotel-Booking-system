from django.contrib import admin
from .models import Sign_up

class register(admin.ModelAdmin):
    list_display = ("name","username","Phone_Number","email","password")
    
admin.site.register(Sign_up, register)