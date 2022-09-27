from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # User은 first,last name을 안쓰는데 이놈은 쓴다
    fieldsets = (
        (
            'profile',
            {
                'fields':('username','password','name','email','is_host'),
                'classes':('wide',),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                'classes':("collapse",)
            },
        ),
        (
            'Important Dates',{"fields": ("last_login", "date_joined"),
                'classes':("collapse",),
                },
        ),
    )
    
    list_display = ['username','email','name','is_host']