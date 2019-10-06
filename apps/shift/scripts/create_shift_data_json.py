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
    members = Member.objects.filter(name__in=member_names).order_by('belong__id', 'grade__id')
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
    assert len(data) % 2 == 0  # フロント側の都合で偶数である必要あり
    return data


def create_shift_data_json(sheet_id, filename='static/json/shift_data.json', return_json=False):
    """シートIDからそのシートのシフトデータを辞書orJSONで返す"""
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
        # 最初のタスクまでの空セルを追加する
        if start_time_id != cells[0].time.id:
            while start_time_id != cells[0].time.id:
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
            # 次のタスクまで空セルを追加する
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
            # 今のタスク名と次のタスク名が同一ならセルを伸ばす
            if i != len(cells)-1 and cell.task.name == cells[i+1].task.name and cell.time.id+1 == cells[i+1].time.id:
                n_cell += 1
                continue
            else:
                end_time = cell.time.end_time
                end_time_id = cell.time.id
                # 同じ時間帯のメンバーを取得
                # members = []の時はネイティブ側でAPIを叩くようにしている
                members = []
                # if return_json:
                #     members = []
                # else:
                #     members = get_same_time_members(sheet_name, cell.task.name, start_time_id, end_time_id)

                # セルを追加
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
    """シートIDを入力させてからシフトデータを作成する"""
    res = input('''Input sheet IDs (1-8) connect each with a comma (ex. 1,2).
All sheet are registered when input 0.
  0: 全て
  1: 準備日晴れ
  2: 準備日雨
  3: 1日目晴れ
  4: 1日目雨
  5: 2日目晴れ
  6: 2日目雨
  7: 片付け日晴れ
  8: 片付け日雨
> ''')
    input_ids = res.replace(' ', '').split(',')
    sheet_ids = ['1', '2', '3', '4', '5', '6', '7', '8']
    if len(input_ids) == 1 and input_ids[0] == '0':
        pass
    elif not all([input_id in sheet_ids for input_id in input_ids]):
        print('Invalid')
        return
    else:
        sheet_ids = input_ids

    for sheet_id in sheet_ids:
        sheet_id = int(sheet_id)
        filename = f'static/json/shift_data_{sheet_id}.json'
        print(f'Saving shift data to {filename}...')
        create_shift_data_json(sheet_id, filename)
