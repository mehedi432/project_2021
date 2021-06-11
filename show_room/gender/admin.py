from django.contrib import admin
from .models import Gender


@admin.register(Gender)
class Gender(admin.ModelAdmin):
    pass