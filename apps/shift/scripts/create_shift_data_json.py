import json
from tqdm import tqdm
from apps.shift.models import Sheet, Member, Cell


def get_same_time_members(sheet_name, task_name, start_time_id, end_time_id):
    """同じ時間帯のメンバーリストを返す"""
    same_time_cells = Cell.objects.filter(sheet__name=sheet_name,
                                          task__name=task_name,
                                          time_id__gte=start_time_id,
                                          time_id__lte=end_time_id)
    if not same_time_cells:
        return []
    member_names = list(set([cell.member.name for cell in same_time_cells]))
    members = Member.objects.filter(name__in=member_names).order_by('belong__id', '-grade__id')
    data = []
    for member in members:
        data.append({
            'name': member.name,
            'belong': member.belong.category_name,
            'grade': member.grade.name,
        })
    if len(members) % 2 != 0:
        data.append({
            'name': '',
            'belong': '',
            'grade': '',
        })
    return data


def create_shift_data_json(sheet_id, filename='static/json/shift_data.json', return_json=False):
    """シフト表示用JSONを作成. return_jsonがFalseのときJSONファイルを保存し，TrueのときJSONオブジェクトを返す."""
    sheet_name = Sheet.objects.get(id=sheet_id).name
    assert sheet_name in Sheet.objects.values_list('name', flat=True)

    data = []
    for member in tqdm(Member.objects.all().order_by('belong__id')):
        name = member.name
        tasks = []
        start_time_id = 1
        end_time_id = 1
        cells = Cell.objects.filter(sheet__name=sheet_name, member__name=name).order_by('time__id')
        if not cells:
            continue
        if start_time_id != cells[0].time.id:
            while start_time_id != cells[0].time.id:
                # 最初の空白セルを追加する
                tasks.append({
                    'name': '',
                    'description': '',
                    'n_cell': 1,
                    'place': '',
                    'color': '',
                    'manual_url': '',
                    'time': '',
                    'start_time_id': start_time_id,
                    'end_time_id': end_time_id,
                    'members': [],
                })
                start_time_id += 1
                end_time_id += 1

        n_cell = 1
        start_time = ''
        for i, cell in enumerate(cells):
            if n_cell == 1:
                start_time = cell.time.start_time
                start_time_id = cell.time.id
            if start_time_id > end_time_id + 1:
                while start_time_id != end_time_id + 1:
                    tasks.append({
                        'name': '',
                        'description': '',
                        'n_cell': 1,
                        'place': '',
                        'color': '',
                        'manual_url': '',
                        'time': '',
                        'start_time_id': end_time_id + 1,
                        'end_time_id': end_time_id + 1,
                        'members': [],
                    })
                    end_time_id += 1
            if i != len(cells) - 1 and cell.task.name == cells[i+1].task.name:
                n_cell += 1
                continue
            else:
                end_time = cell.time.end_time
                end_time_id = cell.time.id
                if return_json:
                    members = []
                else:
                    members = get_same_time_members(sheet_name, cell.task.name, start_time_id, end_time_id)

                tasks.append({
                    'name': cell.task.name,
                    'description': cell.task.description,
                    'n_cell': n_cell,
                    'place': cell.task.place,
                    'color': cell.task.color,
                    'manual_url': cell.task.manual_url,
                    'time': '{} ~ {}'.format(start_time.strftime('%H:%M'), end_time.strftime('%H:%M')),
                    'start_time_id': start_time_id,
                    'end_time_id': end_time_id,
                    'members': members,
                })
                n_cell = 1

        data.append({
            'name': name,
            'belong': {
                'category_name': member.belong.category_name,
                'subcategory_name': member.belong.subcategory_name,
                'short_name': member.belong.short_name,
                'color': member.belong.color,
            },
            'tasks': tasks
        })
    response = {'sheet_name': sheet_name, 'data': data}

    if return_json:
        return response

    with open(filename, 'w') as f:
        json.dump(response, f, ensure_ascii=False)


def main():
    sheet_ids = [3, 4, 5, 6]
    for sheet_id in sheet_ids:
        filename = f'static/json/shift_data_{sheet_id}.json'
        print(f'Saving shift data to {filename}...')
        create_shift_data_json(sheet_id, filename)
