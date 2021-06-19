from django.db import models
from tinymce.models import HTMLField


class Category(models.Model):
    CATEGORY_CHOICES = (
        ('mobile', 'Mobile'),
        ('computer', 'Computer'),
        ('hardware', 'Hardware'),
        ('programming', 'Programming')
    )
    category_name = models.CharField(choices=CATEGORY_CHOICES, max_length=144)
    category_image = models.ImageField(default='default.jpg', upload_to='article/')

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.category_name


class Tag(models.Model):
    article_tag = models.CharField(max_length=21)

    def __str__(self):
        return self.article_tag


class Article(models.Model):
    article_name = HTMLField()
    article_short_text = HTMLField()
    article_image = models.ImageField(default='default.jpg', upload_to='article')
    article_upload_date = models.DateField(auto_now_add=False)
    article_writer = models.CharField(max_length=21)
    article_category = models.ForeignKey("Category", on_delete=models.SET_DEFAULT, default='-')
    article_tag = models.ManyToManyField(Tag)
    article_long_text = HTMLField()

    def __str__(self):
        return self.article_name