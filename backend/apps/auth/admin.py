from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.auth.models import User


@admin.register(User)
class RentHubUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("RentHub", {"fields": ("role", "nickname", "phone", "avatar", "idCardNo")}),)
    list_display = ("username", "role", "nickname", "phone", "is_staff")

