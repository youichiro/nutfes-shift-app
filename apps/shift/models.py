from django.db import models


class Belong(models.Model):
    """部署モデル"""
    id = models.AutoField(primary_key=True)
    category_name = models.CharField('局', max_length=30)
    subcategory_name = models.CharField('部門', null=True, blank=True, max_length=30)
    short_name = models.CharField('略称', max_length=30)
    color = models.CharField('局・部門カラー', max_length=30, default='black')
    order = models.IntegerField('優先順位')

    class Meta:
        db_table = 'belongs'
        verbose_name_plural = '局・部門'
        verbose_name = '局・部門'

    def __str__(self):
        return '{}-{}'.format(self.category_name, self.subcategory_name)


class Department(models.Model):
    """学科モデル"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('学科', max_length=30)

    class Meta:
        db_table = 'departments'
        verbose_name_plural = '学科'
        verbose_name = '学科'

    def __str__(self):
        return self.name


class Grade(models.Model):
    """学年モデル"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('学年', max_length=30)
    order = models.IntegerField('優先順位')

    class Meta:
        db_table = 'grades'
        verbose_name_plural = '学年'
        verbose_name = '学年'

    def __str__(self):
        return self.name


class Member(models.Model):
    """局員モデル"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('名前', max_length=100)
    email = models.EmailField('メールアドレス', unique=True)
    student_id = models.CharField('学籍番号', max_length=8, unique=True)
    belong = models.ForeignKey(Belong, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT)
    is_leader = models.BooleanField('局長/部門長', default=False)
    is_subleader = models.BooleanField('副局長/副部門長', default=False)

    class Meta:
        db_table = 'members'
        verbose_name_plural = '局員'
        verbose_name = '局員'

    def __str__(self):
        return self.name


class Sheet(models.Model):
    """シートモデル"""
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


class Time(models.Model):
    """時間帯モデル"""
    id = models.AutoField(primary_key=True)
    start_time = models.TimeField('開始時刻', unique=True)
    end_time = models.TimeField('終了時刻', unique=True)
    row_number = models.IntegerField('行番号', unique=True)
    is_now = models.BooleanField('現在時刻かどうか', default=False)

    class Meta:
        db_table = 'times'
        verbose_name_plural = '時間帯'
        verbose_name = '時間帯'

    def __str__(self):
        return "{}:{}-{}:{}".format(
            str(self.start_time.hour).rjust(2, '0'),
            str(self.start_time.minute).rjust(2, '0'),
            str(self.end_time.hour).rjust(2, '0'),
            str(self.end_time.minute).rjust(2, '0'),
        )

    @staticmethod
    def first_row_number():
        return min(Time.objects.values_list('row_number', flat=True))

    @staticmethod
    def last_row_number():
        return max(Time.objects.values_list('row_number', flat=True))


class Task(models.Model):
    """タスクモデル"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('タスク名', max_length=100, unique=True)
    description = models.TextField('タスクの説明', null=True, blank=True)
    place = models.CharField('タスクの場所', max_length=100, null=True, blank=True)
    color = models.CharField('タスクの色', max_length=30, default='white')
    manual_url = models.CharField('マニュアルURL', max_length=30, default='')

    class Meta:
        db_table = 'tasks'
        verbose_name_plural = 'タスク'
        verbose_name = 'タスク'

    def __str__(self):
        return self.name


class Cell(models.Model):
    """セルモデル"""
    id = models.AutoField(primary_key=True)
    sheet = models.ForeignKey(Sheet, on_delete=models.PROTECT)
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    time = models.ForeignKey(Time, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)

    class Meta:
        db_table = 'cells'
        unique_together = (("sheet", "member", "time"),)
        verbose_name_plural = 'シフト'
        verbose_name = 'シフト'

    def __str__(self):
        return "{}_{}_{}時{}分_{}".format(
            self.sheet.name,
            self.member.name,
            str(self.time.start_time.hour).rjust(2, '0'),
            str(self.time.start_time.minute).rjust(2, '0'),
            self.task.name
        )
