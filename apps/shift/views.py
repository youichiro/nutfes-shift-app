import json
from django.http import JsonResponse
from django.conf import settings
from apps.shift.scripts.create_shift_data_json import create_shift_data_json


def shift_data_json(request, sheet_id):
    if settings.LOADING_API:
        response = create_shift_data_json(sheet_id, return_json=True)
    else:
        filename = f'static/json/shift_data_{sheet_id}.json'
        with open(filename) as f:
            response = json.load(f)

    response = json.dumps(response, ensure_ascii=False)
    return JsonResponse(response, safe=False)
