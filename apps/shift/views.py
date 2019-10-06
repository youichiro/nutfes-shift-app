import json
from django.http import JsonResponse
from django.conf import settings
from apps.shift.scripts.create_shift_data_json import create_shift_data_json, get_same_time_members
from apps.shift.scripts.create_member_json import create_member_json
from apps.shift.scripts.create_my_shift_data_json import create_my_shift_data_json
from apps.shift.scripts.create_task_shift_data_json import create_task_shift_data_json
from apps.shift.models import Member, Sheet
from apps.option.models import Option


def shift_data_json(request, sheet_id):
    """シフトデータをJSONで返す"""
    option = Option.objects.first()
    api_mode = option.api_mode if option else settings.API_MODE
    if api_mode:
        response = create_shift_data_json(sheet_id, return_json=True)
    else:
        filename = f'static/json/shift_data_{sheet_id}.json'
        with open(filename) as f:
            response = json.load(f)

    response = json.dumps(response, ensure_ascii=False)
    return JsonResponse(response, safe=False)


def same_time_members_json(request, sheet_name, task_name, start_time_id, end_time_id):
    """同じ時間帯のシフトデータをJSONで返す"""
    response = get_same_time_members(sheet_name, task_name, start_time_id, end_time_id)
    response = json.dumps(response, ensure_ascii=False)
    return JsonResponse(response, safe=False)


def is_nutfes_email(request, email):
    """emailがMemberモデルに含まれているかどうかを返す"""
    member = Member.objects.filter(email=email).first()
    if member:
        response = json.dumps(member.name, ensure_ascii=False)
    else:
        response = False
    return JsonResponse(response, safe=False)


def members_json(request):
    """メンバー一覧をJSONで返す"""
    option = Option.objects.first()
    api_mode = option.api_mode if option else settings.API_MODE
    if api_mode:
        response = create_member_json(return_json=True)
    else:
        filename = 'static/json/members.json'
        with open(filename) as f:
            response = json.load(f)

    response = json.dumps(response, ensure_ascii=False)
    return JsonResponse(response, safe=False)


def my_shift_data_json(request, member_name):
    """個人シフトデータをJSONで返す"""
    option = Option.objects.first()
    api_mode = option.api_mode if option else settings.API_MODE
    if api_mode:
        response = []
        for sheet in Sheet.objects.all():
            response.append(
                create_my_shift_data_json(sheet.name, member_name, return_json=True)
            )
    else:
        response = []
        for sheet in Sheet.objects.all():
            filename = f'static/json/my_shift_data/{sheet.id}/{member_name}.json'
            with open(filename) as f:
                response.append(json.load(f))

    response = json.dumps(response, ensure_ascii=False)
    return JsonResponse(response, safe=False)


def task_shift_data_json(request, sheet_id, task_name):
    """タスクシフトデータをJSONで返す"""
    # JSON作成に時間がかかるのでJSONモードは使用しない
    response = create_task_shift_data_json(sheet_id, task_name, return_json=True)
    response = json.dumps(response, ensure_ascii=False)
    return JsonResponse(response, safe=False)
