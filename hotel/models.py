from django.db import models
from django.template.defaultfilters import slugify
from unidecode import unidecode


class Region(models.Model):
    name = models.CharField('название региона',
                            max_length=256)
    description = models.TextField('описание региона',
                                   blank=True,
                                   null=True,
                                   default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('публикация',
                                       default=False)
    num = models.IntegerField('кол-во опубликованных отелей этого региона',
                              default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def save(self, *args, **kwargs):
        if not self.num:
            self.num = counter(self.name, self.num)
            print(self.num)
        super(Region, self).save(*args, **kwargs)


class Hotel(models.Model):
    name = models.CharField('название отеля',
                            max_length=256)
    slug = models.SlugField(max_length=40, blank=True, null=True, default=None,
                            unique=True)
    region = models.ForeignKey(Region, verbose_name='название региона')
    address = models.CharField('адрес отеля',
                               max_length=256)
    images = models.ImageField('фото',
                               upload_to='hotel_images/', blank=True, null=True,
                               default=None)
    description = models.TextField('описание',
                                   blank=True, null=True, default=None)
    price = models.IntegerField('цена отеля', default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.region.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super(Hotel, self).save(*args, **kwargs)


def counter(sel, n):
    n = 0
    all_objects = Hotel.objects.all()
    for item in all_objects.filter(is_published=True):
        if str(sel) == str(item):
            n = n + 1
    return(n)
