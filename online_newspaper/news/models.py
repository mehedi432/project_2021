from __future__ import unicode_literals
from django.db import models


# Create your models here.
class News(models.Model):

    name = models.CharField(max_length=21)
    short_text = models.TextField(default='-')
    long_text = models.TextField(default='-')
    category = models.TextField(default='-')
    category_id = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    publish_date = models.CharField(max_length=13, default='-')
    publish_time = models.CharField(max_length=13, default='0')
    picture_name = models.TextField()
    picture_url = models.TextField(default='-')
    writer = models.CharField(max_length=21, default='-')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'News'
    