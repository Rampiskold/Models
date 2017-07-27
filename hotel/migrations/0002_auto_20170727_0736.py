# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Описание региона'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name_region',
            field=models.CharField(max_length=256, verbose_name='Название региона'),
        ),
    ]