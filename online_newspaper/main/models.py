from __future__ import unicode_literals
from django.db import models


class Main(models.Model):
    name = models.CharField(max_length=21)
    fb = models.CharField(default='-', max_length=21)
    tw = models.CharField(default='-', max_length=21)
    yt = models.CharField(default='-', max_length=21)
    contact = models.CharField(default='-', max_length=21)
    about = models.TextField(default='-')

    set_name = models.CharField(default='Site Settings', max_length=21)

    def __str__(self):
        return self.set_name + " | " + str(self.pk)
