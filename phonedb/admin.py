from django.contrib import admin
from .models import PhoneNumber, UpdatePhoneNumber


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ("code", "start_range", "end_range", "operator", "region", "gar_territory", "inn")


@admin.register(UpdatePhoneNumber)
class UpdatePhoneNumberAdmin(admin.ModelAdmin):
    list_display = ("code", "start_range", "end_range", "operator", "region", "gar_territory", "inn")
