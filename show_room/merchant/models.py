import merchant
from django.db import models


class Merchant(models.Model):
    merchant_name = models.CharField(max_length=55)
    merchant_designation = models.CharField(max_length=55)
    merchant_mobile = models.CharField(max_length=21)
    merchant_email = models.EmailField()
    merchant_join_date = models.DateField(auto_now_add=False)
    merchant_image = models.ImageField(default='default.jpg', upload_to='product/merchant')

    def __str__(self):
        return self.merchant_name