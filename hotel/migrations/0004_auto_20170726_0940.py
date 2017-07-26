# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_hotel_name_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='images_hotel',
            field=models.ImageField(upload_to='hotel_images/'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='price_hotel',
            field=models.IntegerField(default=5000),
        ),
    ]
