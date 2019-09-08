import openpyxl as xl
import shutil
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()

parser.add_argument('--filename', required=True)
parser.add_argument('--output_dir', default='static/xlsx')

args = parser.parse_args()

_IMPORT_FILE_NAME   = args.filename
_IMPORT_FILE_COPY   = "copy.xlsx"
_FRI_SUN_FILE_NAME  = "fri_sunny_shift.xlsx"
_FRI_RAIN_FILE_NAME = "fri_rain_shift.xlsx"
_SAT_SUN_FILE_NAME  = "sat_sunny_shift.xlsx"
_SAT_RAIN_FILE_NAME = "sat_rain_shift.xlsx"
_SUN_SUN_FILE_NAME  = "sun_sunny_shift.xlsx"
_SUN_RAIN_FILE_NAME = "sun_rain_shift.xlsx"
_MON_SUN_FILE_NAME  = "mon_sunny_shift.xlsx"
_MON_RAIN_FILE_NAME = "mon_rain_shift.xlsx"

_TUE_SHEET_NAME      = "準々備日"
_FRI_SUN_SHEET_NAME  = "準備日晴れ"
_FRI_RAIN_SHEET_NAME = "準備日雨"
_SAT_SUN_SHEET_NAME  = "1日目晴れ"
_SAT_RAIN_SHEET_NAME = "1日目雨"
_SUN_SUN_SHEET_NAME  = "2日目晴れ"
_SUN_RAIN_SHEET_NAME = "2日目雨"
_MON_SUN_SHEET_NAME  = "片付け日"
_MON_RAIN_SHEET_NAME = "片付け日"

_DELETE_SHEET_NAME = [
    '準々備日',
    '準備日晴れ',
    '準備日雨',
    '1日目晴れ',
    '1日目雨',
    '2日目晴れ',
    '2日目雨',
    '片付け日',
    '片付け日'
]


def delete_and_output(wb, sheet, file):
    for j in range(len(wb.sheetnames)):
        if _DELETE_SHEET_NAME[j] != sheet:
            wb.remove(wb[_DELETE_SHEET_NAME[j]])
    wb.save(args.output_dir + '/' + file)


book = xl.load_workbook(_IMPORT_FILE_NAME)

for i in tqdm(range(len(book.sheetnames))):
    shutil.copy(args.filename, args.output_dir + "/copy.xlsx")
    wb = xl.load_workbook(_IMPORT_FILE_COPY)

    if book.worksheets[i].title == _FRI_SUN_SHEET_NAME:
        delete_and_output(wb, _FRI_SUN_SHEET_NAME, _FRI_SUN_FILE_NAME)
        continue
    elif book.worksheets[i].title == _FRI_RAIN_SHEET_NAME:
        delete_and_output(wb, _FRI_RAIN_SHEET_NAME, _FRI_RAIN_FILE_NAME)
        continue
    elif book.worksheets[i].title == _SAT_SUN_SHEET_NAME:
        delete_and_output(wb, _SAT_SUN_SHEET_NAME, _SAT_SUN_FILE_NAME)
        continue
    elif book.worksheets[i].title == _SAT_RAIN_SHEET_NAME:
        delete_and_output(wb, _SAT_RAIN_SHEET_NAME, _SAT_RAIN_FILE_NAME)
        continue
    elif book.worksheets[i].title == _SUN_SUN_SHEET_NAME:
        delete_and_output(wb, _SUN_SUN_SHEET_NAME, _SUN_SUN_FILE_NAME)
        continue
    elif book.worksheets[i].title == _SUN_RAIN_SHEET_NAME:
        delete_and_output(wb, _SUN_RAIN_SHEET_NAME, _SUN_RAIN_FILE_NAME)
        continue
    elif book.worksheets[i].title == _MON_SUN_SHEET_NAME:
        delete_and_output(wb, _MON_SUN_SHEET_NAME, _MON_SUN_FILE_NAME)
        ws = wb.active
        ws.title = '片付け日晴れ'
        wb.save(args.output_dir + '/' + _MON_SUN_FILE_NAME)
        continue
    elif book.get_sheet_by_name(_MON_SUN_SHEET_NAME).title == _MON_RAIN_SHEET_NAME:
        delete_and_output(wb, _MON_RAIN_SHEET_NAME, _MON_RAIN_FILE_NAME)
        ws = wb.active
        ws.title = '片付け日雨'
        wb.save(args.output_dir + '/' + _MON_RAIN_FILE_NAME)
