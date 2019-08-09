import json
from .models import TimeTable
from django.http import JsonResponse


def create_timetable_json(request):
    sheet_names = TimeTable.objects.values_list('sheet_name', flat=True)
    sheet_names = list(dict.fromkeys(sheet_names))
    response = []

    for sheet_name in sheet_names:
        places = TimeTable.objects.filter(sheet_name=sheet_name).values_list('place', flat=True)
        places = list(dict.fromkeys(places))
        data = []
        for place in places:
            events = []
            n_cell = 1
            start_time = ''
            cells = TimeTable.objects.filter(sheet_name=sheet_name, place=place).order_by('start_time')
            for i, cell in enumerate(cells):
                if sheet_name == '一日目晴れ' and place == 'メインステージ':
                if n_cell == 1:
                    start_time = cell.start_time
                if i != len(cells) - 1 and cell.event.name == cells[i+1].event.name:
                    n_cell += 1
                    continue
                else:
                    events.append({
                        'name': cell.event.name,
                        'start_time': start_time,
                        'end_time': cell.end_time,
                        'n_cell': n_cell,
                        'color': cell.event.color
                    })
                    n_cell = 1
            data.append({
                'place': place,
                'events': events
            })
        response.append({
            'sheet_name': sheet_name,
            'data': data
        })

    response = json.dumps(response, ensure_ascii=False)
    return JsonResponse(response, safe=False)
