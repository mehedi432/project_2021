from django.contrib import admin
from .models import SubCategory


# Register your models here.
@admin.register(SubCategory)
class SubCategoryModel(admin.ModelAdmin):
    pass