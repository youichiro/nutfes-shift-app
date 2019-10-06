from django.db import models


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('イベント名', null=True, blank=True, max_length=100)
    color = models.CharField('カラー', default='white', max_length=100)

    class Meta:
        db_table = 'events'
        verbose_name_plural = 'イベント'
        verbose_name = 'イベント'

    def __str__(self):
        return self.name if self.name else 'None'


class TimeTable(models.Model):
    id = models.AutoField(primary_key=True)
    sheet_name = models.CharField('シート名', max_length=30)
    place = models.CharField('場所', max_length=30)
    start_time = models.CharField('開始時間', max_length=10)
    end_time = models.CharField('終了時間', max_length=10)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)

    class Meta:
        db_table = 'timetables'
        verbose_name_plural = 'タイムテーブル'
        verbose_name = 'タイムテーブル'

    def __str__(self):
        return '{}_{}_{}~{}_{}'.format(
            self.sheet_name, self.place, self.start_time, self.end_time, self.event
        )
