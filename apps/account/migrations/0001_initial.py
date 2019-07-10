# Generated by Django 2.1 on 2019-06-16 15:56

import apps.account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='メールアドレス')),
                ('is_staff', models.BooleanField(default=False, help_text='管理画面にアクセスすることができる.', verbose_name='スタッフ権限')),
                ('is_active', models.BooleanField(default=True, help_text='有効なユーザである.', verbose_name='有効なユーザ')),
                ('is_superuser', models.BooleanField(default=False, help_text='全ての権限を持っている.', verbose_name='スーパーユーザ権限')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'ユーザ',
                'verbose_name_plural': 'ユーザ',
                'db_table': 'users',
            },
            managers=[
                ('objects', apps.account.models.UserManager()),
            ],
        ),
    ]
