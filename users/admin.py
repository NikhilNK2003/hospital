from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type', 'address_line1', 'city', 'state', 'pincode', 'profile_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type', 'address_line1', 'city', 'state', 'pincode', 'profile_picture')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
