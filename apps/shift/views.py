import json
from django.http import JsonResponse
from django.conf import settings
from apps.shift.scripts.create_shift_data_json import create_shift_data_json, get_same_time_members
from apps.shift.models import Member
from apps.option.models import Option


def shift_data_json(request, sheet_id):
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
    response = get_same_time_members(sheet_name, task_name, start_time_id, end_time_id)
    response = json.dumps(response, ensure_ascii=False)
    return JsonResponse(response, safe=False)


def is_nutfes_email(request, email):
    member = Member.objects.filter(email=email).first()
    if member:
        response = json.dumps(member.name, ensure_ascii=False)
    else:
        response = False
    return JsonResponse(response, safe=False)
