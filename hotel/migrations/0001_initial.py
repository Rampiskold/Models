# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_hotel', models.CharField(max_length=256)),
                ('address_hotel', models.CharField(max_length=256)),
                ('images_hotel', models.ImageField(upload_to=b'hotel_images/')),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('short_description', models.TextField(blank=True, default=None, null=True)),
                ('price_hotel', models.IntegerField(default=0)),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('date_of_change', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u041e\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u041e\u0442\u0435\u043b\u0438',
            },
        ),
    ]