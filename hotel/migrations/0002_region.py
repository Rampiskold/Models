# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_region', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('date_of_change', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0433\u0438\u043e\u043d',
                'verbose_name_plural': '\u0420\u0435\u0433\u0438\u043e\u043d\u044b',
            },
        ),
    ]
