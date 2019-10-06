# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from apps.notification.scripts.create_next_push_requests import main


class Command(BaseCommand):
    help = '次のタスクのPOSTデータをJSONファイルで作成するコマンド'

    def handle(self, *args, **options):
        main()
