from django.core.management.base import BaseCommand
from apps.shift.scripts.member_register import main


class Command(BaseCommand):
    help = '名簿をデータベースに保存するコマンド'

    def handle(self, *args, **options):
        main()
