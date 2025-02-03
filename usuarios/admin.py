from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin 

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = [
        'name',
        'email',
        'date_joined',
        'is_staff',
        'is_superuser',
    ]

    list_filter = [
        'is_staff',
        'is_active',
        'is_superuser',
    ]

    search_fields = [
        'email',
        'name',
    ]

    ordering = ['email']


# Garante que o Django use as configurações da classe CustomUserAdmin
admin.site.register(User, CustomUserAdmin)