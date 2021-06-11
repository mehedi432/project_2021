from django.db import models


class Category(models.Model):
    CHOICE_FIELD = (
        ('cardigan', "Cardigan"),
        ('pullover', "Pullover"),
        ('vest', "Vest")
    )
    category_name = models.CharField(choices=CHOICE_FIELD, max_length=34, null=True, blank=True)
    category_image = models.ImageField(default='default.jpg', upload_to='product/category')

    class Meta():
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name