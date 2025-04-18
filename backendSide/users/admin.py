from django.contrib import admin
from .models import UserProfie
# Register your models here.
@admin.register(UserProfie)
class UserProfileAdmin(admin.ModelAdmin):
    ...