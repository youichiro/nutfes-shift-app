from django.core.management.base import BaseCommand
from apps.timetable.scripts.create_timetable_data_json import main


class Command(BaseCommand):
    help = 'タイムテーブルデータをJSONファイルに保存するコマンド'

    def handle(self, *args, **options):
        main()
