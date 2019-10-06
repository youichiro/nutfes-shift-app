# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from apps.notification.scripts.send_notifications import main


class Command(BaseCommand):
    help = '通知データを読み込んで送信するコマンド'

    def handle(self, *args, **options):
        main()
