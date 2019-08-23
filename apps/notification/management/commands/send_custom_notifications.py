# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from apps.notification.scripts.send_notifications import post_request
from apps.notification.models import DeviceToken


class Command(BaseCommand):
    help = 'テキストを入力して通知を送信するコマンド'

    def add_arguments(self, parser):
        parser.add_argument('title')
        parser.add_argument('body')

    def handle(self, *args, **options):
        assert options['body']
        for device_token in DeviceToken.uniq_list():
            token = device_token.token
            data = {
                'to': token,
                'title': options.get('title', ''),
                'body': options['body'],
                'data': {
                    'title': options.get('title', ''),
                    'body': options['body'],
                }
            }
            post_request(data)
