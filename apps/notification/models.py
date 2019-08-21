from django.db import models


class DeviceToken(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField('トークン', max_length=100)
    username = models.CharField('ユーザ名', max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'device_tokens'
        verbose_name_plural = 'デバイストークン'
        verbose_name = 'デバイストークン'

    def __str__(self):
        return f'{self.username} {self.token}'
