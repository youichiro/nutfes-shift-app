# Generated by Django 2.1.4 on 2019-01-04 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190104_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=models.CharField(help_text='8桁の学籍番号を入力してください.', max_length=8, unique=True, verbose_name='学籍番号'),
        ),
    ]
