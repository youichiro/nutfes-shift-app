# -*- coding: utf-8 -*-
import json
import datetime
from apps.shift.models import Time, Cell, Sheet
from apps.notification.models import DeviceToken
from apps.option.models import Option


def create_next_push_requests(sheet_id, filename):
    """各人の次のシフトを取得してJSONファイルに保存する"""
    requests = []
    current_time = Time.get_current_time()
    for device_token in DeviceToken.uniq_list():
        token = device_token.token
        username = device_token.username
        current_cell = Cell.objects.filter(sheet_id=sheet_id, member__name=username, time=current_time).first()
        if not current_cell:
            continue
        next_cell = Cell.objects.filter(sheet_id=sheet_id, member__name=username, time_id=current_time.id+1).first()
        if not next_cell or current_cell.task.name == next_cell.task.name:
            continue
        next_task = next_cell.task.name

        requests.append({
            'to': token,
            'title': '5分前です',
            'body': f'次のタスクは「{next_task}」です.',
            'data': {
                'title': f'5分前です',
                'body': f'次のタスクは「{next_task}」です'
            }
        })

    with open(filename, 'w') as f:
        json.dump(requests, f, ensure_ascii=False, indent=2)
    print(f'Saved push requests to {filename}')


def get_sheet_id():
    """今日の日付に対応するシートIDを取得すr"""
    today = datetime.datetime.today()
    month = today.month
    day = today.day
    weather = Option.objects.first().weather
    sheet = Sheet.objects.filter(day=day, weather=weather).first()
    if month == 9 and sheet:
        sheet_id = sheet.id
    else:
        sheet_id = 3  # default
    return sheet_id


def main():
    sheet_id = get_sheet_id()
    print('sheet_name:', Sheet.objects.get(id=sheet_id).name)
    filename = 'static/json/next_push_requests.json'
    create_next_push_requests(sheet_id, filename)
