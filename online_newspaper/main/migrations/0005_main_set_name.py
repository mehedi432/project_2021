# Generated by Django 3.2.2 on 2021-05-10 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_main_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='set_name',
            field=models.CharField(default='Site Settings', max_length=21),
        ),
    ]
