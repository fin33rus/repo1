from django.db import models

# Create your models here.

class WahaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Ваха магазин')
    description = models.TextField(verbose_name='Описание')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    url = models.URLField(verbose_name='Интернет-адрес магазина')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ваха магазин'
        verbose_name_plural = 'Ваха магазины'

class WahaGame(models.Model):
    wahashop = models.ForeignKey(WahaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Название игры')
    short_description = models.CharField(max_length=30, verbose_name='Краткое описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    photo = models.ImageField('Фото', upload_to='application1/photos', default='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Ваха игра'
        verbose_name_plural = 'Ваха игры'
        ordering = ['name']
