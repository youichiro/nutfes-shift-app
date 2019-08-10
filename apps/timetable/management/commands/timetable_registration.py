from django.core.management.base import BaseCommand
from apps.timetable.scripts.timetable_register import main


class Command(BaseCommand):
    help = 'タイムテーブルをデータベースに保存するコマンド'

    def handle(self, *args, **options):
        main()
