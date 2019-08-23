import openpyxl
from tqdm import tqdm
from apps.shift.models import Task, Cell, Member, Time


FILES = [
    {
        'filename': "static/xlsx/sat_shift.xlsx",
        'member_range': 'B3:DS3',
        'sheets': [
            {
                'name': '1日目晴れ',
                'sheet_name': '晴',
                'sheet_id': 3,
            },
            {
                'name': '1日目雨',
                'sheet_name': '雨',
                'sheet_id': 4,
            }
        ]
    },
    {
        'filename': 'static/xlsx/sun_shift.xlsx',
        'member_range': 'B3:DE3',
        'sheets': [
            {
                'name': '2日目晴れ',
                'sheet_name': '晴',
                'sheet_id': 5,
            },
            {
                'name': '2日目雨',
                'sheet_name': '雨',
                'sheet_id': 6,
            }
        ]
    },
]


def get_value_list(tuple_2d):
    return [[cell.value for cell in row] for row in tuple_2d]


def column_num_to_alpha(num):
    """列番号をアルファベットに変換(100 -> CV)"""
    i = int((num-1)/26)
    j = int(num-(i*26))
    alpha = ''
    for z in i, j:
        if z != 0:
            alpha += chr(z+64)
    return alpha


def save_and_get_task(name):
    """Taskを登録してインスタンスを返す"""
    if not name:
        return None
    name = name[:100]
    name = name.replace('\n', ' ')
    task, is_created = Task.objects.get_or_create(name=name)
    if is_created:
        task.save()
    return task


def save_cell(sheet_id, member, time, task):
    """Cellを登録する"""
    cell, is_created = Cell.objects.get_or_create(sheet_id=sheet_id, member=member, time=time, task=task)
    if is_created:
        cell.save()


def register(sheet, sheet_id, member_range):
    # 列と局員名の対応辞書を作成
    column2name = {}
    name_cells = sheet[member_range][0]
    for cell in name_cells:
        name = cell.value
        name = name.replace(' ', '').replace('　', '')
        column = cell.col_idx
        column2name[column] = name

    # 結合セルのシフト登録
    merged_cells = sheet.merged_cells.ranges
    for merged_cell in tqdm(merged_cells):
        cell_range = merged_cell.ref
        cells = sheet[cell_range]

        # タスクの登録
        task = get_value_list(cells)[0][0]
        task = save_and_get_task(task)
        if not task:
            continue

        for column_cells in cells:
            for cell in column_cells:
                row = cell.row
                col = cell.col_idx

                # 範囲外のセルは除外する
                if col not in column2name.keys():
                    continue
                if row not in Time.objects.values_list('row_number', flat=True):
                    continue

                name = column2name[col]
                member = Member.objects.filter(name=name)
                if not member:
                    continue
                member = member.first()
                time = Time.objects.get(row_number=row)
                save_cell(sheet_id, member, time, task)

    # 結合セル以外のシフト登録
    all_range = "{}{}:{}{}".format(column_num_to_alpha(min(column2name.keys())),
                                   Time.first_row_number(),
                                   column_num_to_alpha(max(column2name.keys())),
                                   Time.last_row_number())
    all_cells = sheet[all_range]
    for row_cells in tqdm(all_cells):
        for cell in row_cells:
            row = cell.row
            col = cell.col_idx
            name = column2name[col]
            task = cell.value

            # タスクの登録
            task = save_and_get_task(task)
            if not task:
                continue

            member = Member.objects.filter(name=name)
            if not member:
                continue
            member = member.first()
            time = Time.objects.get(row_number=row)
            save_cell(sheet_id, member, time, task)


def main():
    if Cell.objects.first() or Task.objects.first():
        res = input('Do you delete all Cell and Task instances ? [yes/no] ')
        if res == 'yes':
            Cell.objects.all().delete()
            Task.objects.all().delete()
            print('All Cell and Task instances were deleted.')
        else:
            return

    for file in FILES:
        wb = openpyxl.load_workbook(file['filename'])
        member_range = file['member_range']
        for sheet in file['sheets']:
            print(f'Saving {sheet["name"]}...')
            register(sheet=wb[sheet['sheet_name']], sheet_id=sheet['sheet_id'], member_range=member_range)
