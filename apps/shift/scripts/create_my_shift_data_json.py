import json
from tqdm import tqdm
from apps.shift.models import Sheet, Member, Cell
from apps.shift.scripts.create_shift_data_json import get_same_time_members


def create_my_shift_data_json(sheet_name, member_name, filename='static/json/my_shift_data/someone.json', return_json=False):
    """sheet_nameとmember_nameから個人シフトデータを作成して辞書orJSONで返す"""
    tasks = []
    start_time_id = 1
    end_time_id = 1
    cells = Cell.objects.filter(sheet__name=sheet_name, member__name=member_name).order_by('time__id')
    if not cells:
        return

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
        if i != len(cells) - 1 and cell.task.name == cells[i + 1].task.name and cell.time.id + 1 == cells[i + 1].time.id:
            n_cell += 1
            continue
        else:
            end_time = cell.time.end_time
            end_time_id = cell.time.id
            # 同じ時間帯のメンバーを取得
            # members = []の時はネイティブ側でAPIを叩くようにしている
            if return_json:
                members = []
            else:
                members = get_same_time_members(sheet_name, cell.task.name, start_time_id, end_time_id)

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

    member = Member.objects.filter(name=member_name).first()
    response = {
        'sheet_name': sheet_name,
        'name': member_name,
        'category_name': member.belong.category_name,
        'subcategory_name': member.belong.subcategory_name,
        'color': member.belong.color,
        'tasks': tasks,
    }

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

    member_list = Member.objects.all().values_list('name', flat=True)
    for sheet_id in sheet_ids:
        sheet_id = int(sheet_id)
        sheet_name = Sheet.objects.get(id=sheet_id).name
        print(sheet_name)
        for member_name in tqdm(member_list):
            filename = f'static/json/my_shift_data/{sheet_id}/{member_name}.json'
            create_my_shift_data_json(sheet_name, member_name, filename)
    print('Saved my shift data to static/json/my_shift_data directory')
