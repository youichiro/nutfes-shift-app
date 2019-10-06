import json
from django.http import JsonResponse
from apps.option.models import Option


def weather_json(request):
    """weatherをJSONで返す"""
    option = Option.objects.first()
    if option:
        response = json.dumps(option.weather, ensure_ascii=False)
    else:
        response = None
    return JsonResponse(response, safe=False)
