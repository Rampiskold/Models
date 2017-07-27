from django.db import models
from django.core import validators


class Region(models.Model):
    name_region = models.CharField(max_length=256,
                                   verbose_name="Название региона")
    description = models.TextField(blank=True, null=True, default=None,
                                   verbose_name="Описание региона")
    date_of_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_of_change = models.DateTimeField(auto_now_add=False, auto_now=True)
    published_region = models.BooleanField(default=False,
                                           verbose_name="Публикация")

    def __str__(self):
        return self.name_region

    class Meta:
        ordering = ('name_region',)
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class Hotel(models.Model):
    name_hotel = models.CharField(max_length=256, verbose_name="Название отеля")
    # slug = models.SlugField()
    name_region = models.ForeignKey(Region, blank=True, null=True, default=None,
                                    verbose_name="Название региона")
    address_hotel = models.CharField(max_length=256, verbose_name="Адрес отеля")
    images_hotel = models.ImageField(upload_to='hotel_images/',
                                     verbose_name="Фотография отеля")
    description = models.TextField(blank=True, null=True, default=None,
                                   verbose_name="Описание отеля")
    price_hotel = models.IntegerField(default=0, verbose_name="Цена отеля")
    date_of_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_of_change = models.DateTimeField(auto_now_add=False, auto_now=True)
    published_hotel = models.BooleanField(default=False)

    def __str__(self):
        return self.name_hotel

    class Meta:
        ordering = ('name_hotel',)
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'
