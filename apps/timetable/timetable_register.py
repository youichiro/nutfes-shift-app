import openpyxl
import datetime
from .models import TimeTable, Event


COMMON_OPTION = {
    'file_path': 'static/xlsx/timetable.xlsx',
    'final_row_num': 34
}

SHEET_OPTIONS = [
    {
        'sheet_name': '一日目晴れ',
        'place_range': 'C1:L1',
        'active_range': 'C2:L46'
    },
    {
        'sheet_name': '一日目雨',
        'place_range': 'C1:I1',
        'active_range': 'C2:I46'
    },
    {
        'sheet_name': '二日目晴れ',
        'place_range': 'C1:L1',
        'active_range': 'C2:L46'
    },
    {
        'sheet_name': '二日目雨',
        'place_range': 'C1:J1',
        'active_range': 'C2:J46'
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


def save_and_get_event(event_name):
    """Eventを登録してインスタンスを返す"""
    if event_name:
        event_name = event_name.replace('\n', '')
    event, is_created = Event.objects.get_or_create(name=event_name)
    if is_created:
        event.save()
    return event


def save_cell(sheet_name, place, start_time, end_time, event):
    """TimeTableモデルに保存する"""
    timetable, is_created = TimeTable.objects.get_or_create(
        sheet_name=sheet_name, place=place, start_time=start_time, end_time=end_time, event=event
    )
    if is_created:
        timetable.save()


def register(sheet, place_range, active_range):
    # 列と場所の対応辞書を作成
    column2place = {}
    place_cells = sheet[place_range][0]
    for cell in place_cells:
        place = cell.value
        column = cell.col_idx
        column2place[column] = place

    # 結合セルの登録
    merged_cells = sheet.merged_cells.ranges
    for merged_cell in merged_cells:
        cell_range = merged_cell.ref
        cells = sheet[cell_range]
        event_name = get_value_list(cells)[0][0]
        event = save_and_get_event(event_name)

        for column_cells in cells:
            for cell in column_cells:
                row = cell.row
                col = cell.col_idx

                # 範囲外のセルは除外する
                if col not in column2place.keys():
                    continue
                if row > COMMON_OPTION['final_row_num']:
                    continue

                place = column2place[col]
                start_time = sheet['A' + str(row)].value
                if type(start_time) == datetime.time:
                    start_time = start_time.strftime('%H:%M')
                end_time = sheet['B' + str(row)].value
                if type(end_time) == datetime.time:
                    end_time = end_time.strftime('%H:%M')
                save_cell(sheet.title, place, start_time, end_time, event)

    all_cells = sheet[active_range]
    for row_cells in all_cells:
        for cell in row_cells:
            row = cell.row
            col = cell.col_idx
            place = column2place[col]
            event_name = cell.value
            event = save_and_get_event(event_name)
            start_time = sheet['A' + str(row)].value
            if type(start_time) == datetime.time:
                start_time = start_time.strftime('%H:%M')
            end_time = sheet['B' + str(row)].value
            if type(end_time) == datetime.time:
                end_time = end_time.strftime('%H:%M')

            if not event_name and TimeTable.objects.filter(sheet_name=sheet.title, place=place, start_time=start_time):
                continue
            save_cell(sheet.title, place, start_time, end_time, event)


def main():
    wb = openpyxl.load_workbook(COMMON_OPTION['file_path'])
    for sheet_option in SHEET_OPTIONS:
        sheet = wb[sheet_option['sheet_name']]
        print(f'Saving timetable: {sheet_option["sheet_name"]} ...')
        register(sheet, sheet_option['place_range'], sheet_option['active_range'])
