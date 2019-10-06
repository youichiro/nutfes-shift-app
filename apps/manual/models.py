from django.db import models


class Manual(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField('分類', max_length=30)
    title = models.CharField('タイトル', max_length=30)
    url = models.URLField(max_length=1000, null=True, blank=True)
    order = models.IntegerField('順番', null=True, blank=True)

    class Meta:
        db_table = 'manuals'
        verbose_name_plural = 'マニュアル'
        verbose_name = 'マニュアル'

    def __str__(self):
        return self.title
