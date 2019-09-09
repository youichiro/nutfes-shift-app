from django.core.management.base import BaseCommand
from apps.shift.scripts.create_task_shift_data_json import main


class Command(BaseCommand):
    help = 'タスク別シフトデータをJSONファイルに保存するコマンド'

    def handle(self, *args, **options):
        main()
