# Generated by Django 2.1.4 on 2019-01-20 06:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shift', '0002_auto_20190120_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='場所'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='タスク名'),
        ),
        migrations.AlterField(
            model_name='time',
            name='time',
            field=models.TimeField(unique=True, verbose_name='開始時刻'),
        ),
        migrations.AlterUniqueTogether(
            name='cell',
            unique_together={('user', 'time')},
        ),
    ]
