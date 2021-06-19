from django.db import models
from gender.models import Gender
from category.models import Category
from merchant.models import Merchant


# Create your models here.
class Product(models.Model):
    product_style = models.CharField(max_length=21)
    product_composition = models.CharField(max_length=144)
    product_gauge = models.CharField(max_length=13)
    product_size = models.CharField(max_length=13)
    product_weight = models.CharField(max_length=13)
    product_moq = models.CharField(max_length=13)
    product_fob = models.CharField(max_length=13)
    product_category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default="-")
    product_gender = models.ForeignKey(Gender, on_delete=models.SET_DEFAULT, default="-")
    product_merchant = models.ForeignKey(Merchant, on_delete=models.SET_DEFAULT, default="Admin")
    product_buyer = models.IntegerField(default=0)
    product_shipment_date = models.DateField(auto_now_add=False)
    product_quantity = models.IntegerField(default=0)
    product_image = models.ImageField(default='default.jpg', upload_to='product/pro')
    product_chart = models.ImageField(default='default.jpg', upload_to='product/chart')

    def __str__(self):
        return self.product_style