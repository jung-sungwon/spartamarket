from django.contrib import admin

# Register your models here.
# users/admin.py
from django.contrib import admin
from .models import User

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'name', 'nickname', 'birthday', 'is_staff')
    search_fields = ('username', 'email')
