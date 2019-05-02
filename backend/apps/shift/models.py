from django.db import models
from apps.account.models import User


class Sheet(models.Model):
    """シート"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('シート名', max_length=30, help_text='ex) 1日目, 片付け日')
    date = models.DateField('実施日')
    is_active = models.BooleanField('有効なシートかどうか', default=True)

    class Meta:
        db_table = 'sheets'
        verbose_name_plural = 'シート'
        verbose_name = 'シート'

    def __str__(self):
        return self.name


class Place(models.Model):
    """タスクの実施場所"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('場所', max_length=30, unique=True)
    color = models.CharField('場所カラー', max_length=30, default='black')

    class Meta:
        db_table = 'places'
        verbose_name_plural = 'タスクの実施場所'
        verbose_name = 'タスクの実施場所'

    def __str__(self):
        return self.name


class Time(models.Model):
    """時間帯"""
    id = models.AutoField(primary_key=True)
    start_time = models.TimeField('開始時刻', unique=True)
    end_time = models.TimeField('終了時刻', unique=True)
    is_now = models.BooleanField('現在時刻かどうか', default=False)

    class Meta:
        db_table = 'times'
        verbose_name_plural = '時間帯'
        verbose_name = '時間帯'

    def __str__(self):
        return f"{self.start_time}-{self.end_time}"


class Task(models.Model):
    """タスク(業務)"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('タスク名', max_length=30, unique=True)
    description = models.TextField('タスクの説明', null=True, blank=True)
    place = models.ForeignKey(Place, null=True, blank=True, on_delete=models.PROTECT)
    color = models.CharField('タスクの色', max_length=30, default='black')

    class Meta:
        db_table = 'tasks'
        verbose_name_plural = 'タスク'
        verbose_name = 'タスク'

    def __str__(self):
        return self.name


class Cell(models.Model):
    """セル(シフトの1単位)"""
    id = models.AutoField(primary_key=True)
    sheet = models.ForeignKey(Sheet, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    time = models.ForeignKey(Time, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)

    class Meta:
        db_table = 'cells'
        unique_together = (("sheet", "user", "time"),)
        verbose_name_plural = 'シフト'
        verbose_name = 'シフト'

    def __str__(self):
        return f"{self.sheet.name}_{self.user.name}_{self.time.start_time.hour}\
                 時{self.time.start_time.minute}_{self.task.name}"
