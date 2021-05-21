from django.contrib import admin
from .models import Main


# Register your models here.
@admin.register(Main)
class MainModel(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Main'
