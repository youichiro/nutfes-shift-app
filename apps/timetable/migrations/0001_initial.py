# Generated by Django 2.1 on 2019-08-09 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='イベント名')),
                ('color', models.CharField(default='white', max_length=10, verbose_name='カラー')),
            ],
            options={
                'verbose_name': 'イベント',
                'verbose_name_plural': 'イベント',
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sheet_name', models.CharField(max_length=30, verbose_name='シート名')),
                ('place', models.CharField(max_length=30, verbose_name='場所')),
                ('start_time', models.CharField(max_length=10, verbose_name='開始時間')),
                ('end_time', models.CharField(max_length=10, verbose_name='終了時間')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='timetable.Event')),
            ],
            options={
                'verbose_name': 'タイムテーブル',
                'verbose_name_plural': 'タイムテーブル',
                'db_table': 'timetables',
            },
        ),
    ]