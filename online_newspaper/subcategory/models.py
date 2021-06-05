from __future__ import unicode_literals
from django.db import models


class SubCategory(models.Model):
    name = models.CharField(max_length=21)
    category_name = models.CharField(max_length=21)
    category_id = models.IntegerField()


    def __str__(self):
        return self.name