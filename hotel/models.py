# -*- coding: utf-8 -*-
from django.db import models
from django.core import validators


class Region(models.Model):
    name_region = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True, default=None)
    date_of_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_of_change = models.DateTimeField(auto_now_add=False, auto_now=True)

    # published_region = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return " %s;" % self.name_region

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class Hotel(models.Model):
    name_hotel = models.CharField(max_length=256)
    name_region = models.ForeignKey(Region, blank=True, null=True, default=None)
    address_hotel = models.CharField(max_length=256)
    images_hotel = models.ImageField(upload_to='hotel_images/')
    description = models.TextField(blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    price_hotel = models.IntegerField(validators=[validators.MinValueValidator(5000)] ,default=5000)
    date_of_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_of_change = models.DateTimeField(auto_now_add=False, auto_now=True)

    # published_hotel = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Date of creation: %s; Date of change: %s;" % \
               (self.date_of_creation, self.date_of_change,)

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'


        
