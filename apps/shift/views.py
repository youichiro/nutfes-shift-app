import json
from django.http import JsonResponse


def shift_data_json(request, sheet_id):
    filename = f'static/json/shift_data_{sheet_id}.json'
    with open(filename) as f:
        response = json.load(f)

    response = json.dumps(response, ensure_ascii=False)
    return JsonResponse(response, safe=False)
