from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils import timezone
from django.db.utils import IntegrityError
from apps.shift.models import Belong, Department, Grade, Sheet, Time
from apps.option.models import Option


class Command(BaseCommand):
    help = '初期データを登録するコマンド'
    # TODO: add_argumentsで初期化したいモデルを指定できるようにする

    def handle(self, *args, **options):
        try:
            init_department()
            init_grade()
            init_belong()
            init_sheet()
            init_time()
            init_option()
            self.stdout.write('Initialized tables')
        except IntegrityError:
            self.stdout.write('Init data already exists. Run `python manage.py flush` to clean database.')


def init_department():
    """学科の初期化"""
    for i, name in enumerate(settings.DEPARTMENTS):
        Department.objects.create(id=i+1, name=name)


def init_grade():
    """学年の初期化"""
    for i, name in enumerate(settings.GRADES):
        Grade.objects.create(id=i+1, name=name)


def init_belong():
    """所属の初期化"""
    for i, (category_name, subcategory_name, short_name, color) in enumerate(settings.BELONGS):
        Belong.objects.create(id=i+1,
                              category_name=category_name,
                              subcategory_name=subcategory_name,
                              short_name=short_name,
                              color=color)


def init_sheet():
    """シートの初期化"""
    for i, sheet in enumerate(settings.SHEETS):
        Sheet.objects.create(id=i+1, name=sheet['name'], day=sheet['day'], weather=sheet['weather'])


def init_time():
    """開始時間と時間間隔から時間帯(Time)を作成する"""
    # settings.SHIFT_START_TIME: 開始時間 (ex. '06:00:00')
    # settings.SHIFT_START_ROW: 開始時間のスプレッドシートの行番号 (ex. 3)
    # settings.SHIFT_INTERVAL: 時間帯の間隔 (ex. 30)
    # settings.SHIFT_END_TIME: 終了時間 (ex. '23:00:00')

    start_time = '2020-01-01 ' + settings.SHIFT_START_TIME  # 日付はダミー
    start_time = timezone.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')  # strをdatetimeに変換
    row = settings.SHIFT_START_ROW

    # 開始時間の保存
    Time.objects.create(
        id=1,
        start_time=start_time,
        end_time=start_time+timezone.timedelta(minutes=settings.SHIFT_INTERVAL),
        row_number=row
    )

    end_time = '2020-01-01 ' + settings.SHIFT_END_TIME  # 日付はダミー
    end_time = timezone.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')  # strをdatetimeに変換

    # start_timeからend_timeまで時間間隔を加算しながら保存していく
    time = start_time
    while time < end_time:
        time = time + timezone.timedelta(minutes=settings.SHIFT_INTERVAL)
        row += 1
        Time.objects.create(
            start_time=time,
            end_time=time+timezone.timedelta(minutes=settings.SHIFT_INTERVAL),
            row_number=row
        )


def init_option():
    """共通オプションの生成"""
    Option.objects.create(id=1, weather='晴', api_mode=True)
