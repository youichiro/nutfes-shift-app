from django.db import models

WEATHERS = [('晴', '晴'), ('雨', '雨')]


class Option(models.Model):
    id = models.AutoField(primary_key=True)
    weather = models.CharField('天気', max_length=10, choices=WEATHERS, default='晴')
    api_mode = models.BooleanField('APIモードか', default=True)

    class Meta:
        db_table = 'options'
        verbose_name_plural = '共通オプション'
        verbose_name = '共通オプション'
