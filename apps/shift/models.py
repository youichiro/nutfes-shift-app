from django.db import models
from apps.account.models import User


class Sheet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('シート名', max_length=30)
    date = models.DateField('実施日')
    is_active = models.BooleanField('有効なシートかどうか', default=True)

    class Meta:
        db_table = 'sheets'

    def __str__(self):
        return self.name


class Place(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('場所', max_length=30, unique=True)

    class Meta:
        db_table = 'places'

    def __str__(self):
        return self.name


class Time(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.TimeField('開始時刻', unique=True)
    is_now = models.BooleanField('現在時刻かどうか', default=False)

    class Meta:
        db_table = 'times'

    def __str__(self):
        return str(self.time)


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('タスク名', max_length=30, unique=True)
    description = models.TextField('タスクの説明', null=True, blank=True)
    place = models.ForeignKey(Place, null=True, blank=True, on_delete=models.PROTECT)
    color = models.CharField('タスクの色', max_length=30, default='white')

    class Meta:
        db_table = 'tasks'

    def __str__(self):
        return self.name


class Cell(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    time = models.ForeignKey(Time, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)

    class Meta:
        db_table = 'cells'
        unique_together = (("user", "time"),)

    def __str__(self):
        return "{}_{}時{}分_{}".format(self.user.name, self.time.time.hour,
                                     self.time.time.minute, self.task.name)
