from django.core.management.base import BaseCommand
from apps.shift.scripts.create_member_json import main


class Command(BaseCommand):
    help = 'MemberをJSONファイルに保存するコマンド'

    def handle(self, *args, **options):
        main()
