import json
from tqdm import tqdm
from apps.shift.models import Sheet, Member, Cell
from apps.shift.scripts.create_shift_data_json import get_same_time_members


def create_my_shift_data_json(member_name, filename='static/json/my_shift_data/someone.json', return_json=False):
    sheets = []
    for sheet in Sheet.objects.all():
        tasks = []
        start_time_id = 1
        end_time_id = 1
        cells = Cell.objects.filter(sheet=sheet, member__name=member_name).order_by('time__id')
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
                    members = get_same_time_members(sheet.name, cell.task.name, start_time_id, end_time_id)

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

        sheets.append({
            'sheet_name': sheet.name,
            'tasks': tasks,
        })

    member = Member.objects.filter(name=member_name).first()
    response = {
        'name': member_name,
        'category_name': member.belong.category_name,
        'subcategory_name': member.belong.subcategory_name,
        'color': member.belong.color,
        'sheets': sheets,
    }

    if return_json:
        return response

    with open(filename, 'w') as f:
        json.dump(response, f, ensure_ascii=False)


def main():
    member_list = Member.objects.all().values_list('name', flat=True)
    for member_name in tqdm(member_list):
        filename = f'static/json/my_shift_data/{member_name}.json'
        create_my_shift_data_json(member_name, filename)
    print('Saved my shift data to static/json/my_shift_data directory')
