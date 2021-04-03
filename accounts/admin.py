from django.contrib import admin
from accounts.models import *
from django.contrib.auth.admin import UserAdmin


class MyCustomUserAdmin(UserAdmin):
    model = CustomUser
    
    
admin.site.register(CustomUser, MyCustomUserAdmin)




