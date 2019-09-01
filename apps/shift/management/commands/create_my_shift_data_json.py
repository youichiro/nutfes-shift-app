from django.core.management.base import BaseCommand
from apps.shift.scripts.create_my_shift_data_json import main


class Command(BaseCommand):
    help = '個人シフトデータをJSONファイルに保存するコマンド'

    def handle(self, *args, **options):
        main()
