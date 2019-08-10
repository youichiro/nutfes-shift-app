import json
from django.http import JsonResponse


def timetable_json(request):
    filename = 'static/json/timetable.json'
    with open(filename) as f:
        response = json.load(f)

    response = json.dumps(response, ensure_ascii=False)
    return JsonResponse(response, safe=False)
