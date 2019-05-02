from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils import timezone
from django.db.utils import IntegrityError

from apps.account.models import Belong, Department, Grade
from apps.shift.models import Sheet, Place, Time


class Command(BaseCommand):
    help = 'Init database with defined seed data'

    # TODO: add_argumentsで初期化したいモデルを指定できるようにする

    def handle(self, *args, **options):
        try:
            init_department()
            init_grade()
            init_belong()
            init_sheet()
            init_place()
            init_time()
            self.stdout.write('Initialized tables')
        except IntegrityError:
            self.stderr.write('Init data already exists. Run `python manage.py flush` to clean database.')


def init_department():
    """学科の初期化"""
    for i, name in enumerate(settings.DEPARTMENTS):
        Department.objects.create(id=i+1, name=name)


def init_grade():
    """学年の初期化"""
    for i, name in enumerate(settings.GRADES):
        Grade.objects.create(id=i+1, name=name, order=i+1)


def init_belong():
    """所属の初期化"""
    for i, (name, short_name) in enumerate(settings.BELONGS):
        Belong.objects.create(id=i+1, name=name, short_name=short_name, order=i+1)


def init_sheet():
    """シートの初期化"""
    for i, (name, date) in enumerate(settings.FES_DATES):
        Sheet.objects.create(id=i+1, name=name, date=date)


def init_place():
    """場所の初期化"""
    for i, name in enumerate(settings.PLACES):
        Place.objects.create(id=i+1, name=name)


def init_time():
    """時間帯の初期化"""
    start_time = '2020-01-01 ' + settings.SHIFT_START_TIME  # 日付はダミー
    start_time = timezone.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')  # str -> datetime に変換
    # 開始時間の保存
    Time.objects.create(
        id=1,
        start_time=start_time,
        end_time=start_time+timezone.timedelta(minutes=settings.SHIFT_INTERVAL)
    )
    end_time = '2020-01-01 ' + settings.SHIFT_END_TIME  # 日付はダミー
    end_time = timezone.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')  # str -> datetime に変換
    time = start_time
    while time < end_time:
        # 時間間隔を加算しながら保存
        time = time + timezone.timedelta(minutes=settings.SHIFT_INTERVAL)
        Time.objects.create(
            start_time=time,
            end_time=time+timezone.timedelta(minutes=settings.SHIFT_INTERVAL)
        )
