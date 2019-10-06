from django.db import models
from django.conf import settings


class Option(models.Model):
    id = models.AutoField(primary_key=True)
    weather = models.CharField('天気', max_length=10, choices=settings.WEATHERS, default=settings.WEATHERS[0][0])
    api_mode = models.BooleanField('APIモードかどうか', default=True)

    class Meta:
        db_table = 'options'
        verbose_name_plural = '共通オプション'
        verbose_name = '共通オプション'
