# Generated by Django 3.2.2 on 2021-05-10 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210510_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='about',
            field=models.TextField(default='-'),
        ),
    ]