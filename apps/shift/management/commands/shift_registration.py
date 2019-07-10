from django.core.management.base import BaseCommand
from apps.shift.shift_register import main


class Command(BaseCommand):
    help = 'シフトをデータベースに保存するコマンド'

    def handle(self, *args, **options):
        main()
