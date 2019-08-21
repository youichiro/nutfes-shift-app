from django.core.management.base import BaseCommand
from apps.notification.scripts.post_push_requests import main


class Command(BaseCommand):
    help = '通知データを読み込んで通知を送信するコマンド'

    def handle(self, *args, **options):
        main()
