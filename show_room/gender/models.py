from django.db import models


class Gender(models.Model):
    CHOICE_FIELD = (
        ('male', "Male"),
        ('female', "Female"),
        ('boys', "Boys"),
        ('girls', "Girls"),
        ('unisex', "Unisex"),
    )
    gender_name = models.CharField(choices=CHOICE_FIELD, max_length=34, null=True, blank=True)
    gender_image = models.ImageField(default='default.jpg', upload_to='product/gender')

    def __str__(self):
        return self.gender_name