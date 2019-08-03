import json
from .models import Time, Sheet, Member, Cell
from django.http import JsonResponse


def get_shift_data_json(request, sheet_id):
    sheet_name = Sheet.objects.get(id=sheet_id).name
    assert sheet_name in Sheet.objects.values_list('name', flat=True)
    data = []
    for member in Member.objects.all():
        name = member.name
        tasks = []
        cells = Cell.objects.filter(member__name=name, sheet__name=sheet_name)
        if not cells:
            continue
        times = Time.objects.all()
        if cells[0].time.start_time != Time.objects.first():
            i = 1
            n_cell = 1
            while times[i].start_time == cells[0].time.start_time:
                n_cell += 1
                i += 1
            tasks.append({
                'name': '',
                'description': '',
                'n_cell': n_cell
            })

        n_cell = 1
        for i, cell in enumerate(cells):
            if i != len(cells) - 1 and cell.task.name == cells[i+1].task.name:
                n_cell += 1
                continue
            else:
                tasks.append({
                    'name': cell.task.name,
                    'description': cell.task.description,
                    'n_cell': n_cell
                })
                n_cell = 1

        data.append({
            'name': name,
            'belong': {
                'category_name': member.belong.category_name,
                'subcategory_name': member.belong.subcategory_name,
                'short_name': member.belong.short_name
            },
            'tasks': tasks
        })
    response = {'sheet_name': sheet_name, 'data': data}
    response = json.dumps(response, ensure_ascii=False)
    return JsonResponse(response, safe=False)
