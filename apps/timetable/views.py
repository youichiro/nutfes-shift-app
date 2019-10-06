import json
from django.http import JsonResponse
from django.conf import settings
from apps.timetable.scripts.create_timetable_data_json import create_timetable_json
from apps.option.models import Option


def timetable_json(request):
    """TimeTableデータをJSONで返す"""
    option = Option.objects.first()
    api_mode = option.api_mode if option else settings.API_MODE
    if api_mode:
        response = create_timetable_json(return_json=True)
    else:
        filename = 'static/json/timetable.json'
        with open(filename) as f:
            response = json.load(f)

    response = json.dumps(response, ensure_ascii=False)
    return JsonResponse(response, safe=False)
