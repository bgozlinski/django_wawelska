from django.contrib import admin
from users.models import User


@admin.register(User)
class CarAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_phone_number']