from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_style', 'product_composition', 'product_gauge', 'product_size', 'product_weight', 'product_category', 'product_gender')
