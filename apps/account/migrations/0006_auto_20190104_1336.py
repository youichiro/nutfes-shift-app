# Generated by Django 2.1.4 on 2019-01-04 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20190104_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='belong',
            field=models.CharField(help_text='所属している局・部門を選択してください.', max_length=30, verbose_name='所属'),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(help_text='学科を選択してください.', max_length=30, verbose_name='学科'),
        ),
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.CharField(help_text='学年を選択してください.', max_length=30, verbose_name='学年'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='有効なユーザである.', verbose_name='有効なユーザ'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='管理画面にアクセスすることができる.', verbose_name='スタッフ権限'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='全ての権限を持っている.', verbose_name='スーパーユーザ権限'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(help_text='名前を入力してください.', max_length=100, verbose_name='名前'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, help_text='電話番号を入力してください(半角数字のみ).', max_length=11, null=True, verbose_name='電話番号'),
        ),
    ]
