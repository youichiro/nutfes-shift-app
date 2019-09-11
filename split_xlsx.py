import openpyxl
import shutil
import argparse
from tqdm import tqdm


OUTPUT_FILES = [
    {
        'filename': 'fri_sunny_shift.xlsx',
        'sheet_name': '準備日晴れ',
        'org_sheet_name': '準備日晴れ',
    },
    {
        'filename': 'fri_rain_shift.xlsx',
        'sheet_name': '準備日雨',
        'org_sheet_name': '準備日雨',
    },
    {
        'filename': 'sat_sunny_shift.xlsx',
        'sheet_name': '1日目晴れ',
        'org_sheet_name': '1日目晴れ',
    },
    {
        'filename': 'sat_rain_shift.xlsx',
        'sheet_name': '1日目雨',
        'org_sheet_name': '1日目雨',
    },
    {
        'filename': 'sun_sunny_shift.xlsx',
        'sheet_name': '2日目晴れ',
        'org_sheet_name': '2日目晴れ',
    },
    {
        'filename': 'sun_rain_shift.xlsx',
        'sheet_name': '2日目雨',
        'org_sheet_name': '2日目雨',
    },
    {
        'filename': 'mon_sunny_shift.xlsx',
        'sheet_name': '片付け日晴れ',
        'org_sheet_name': '片付け日',
    },
    {
        'filename': 'mon_rain_shift.xlsx',
        'sheet_name': '片付け日雨',
        'org_sheet_name': '片付け日',
    },
]


def extract_sheet(wb, org_sheet_name, save_sheet_name, filename):
    for sheet_name in wb.sheetnames:
        if sheet_name != org_sheet_name:
            wb.remove(wb[sheet_name])
    if org_sheet_name != save_sheet_name:
        ws = wb.active
        ws.title = save_sheet_name
    wb.save(filename)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True,
                        help='ダウンロードしたexcelファイルを指定する')
    parser.add_argument('-o', '--output-dir', default='static/xlsx',
                        help='分割したexcelファイルの保存場所を指定する')
    args = parser.parse_args()

    for output_file in tqdm(OUTPUT_FILES):
        filename = args.output_dir + '/' + output_file['filename']
        sheet_name = output_file['sheet_name']
        org_sheet_name = output_file['org_sheet_name']
        shutil.copy(args.filename, filename)
        wb = openpyxl.load_workbook(filename)
        extract_sheet(wb, org_sheet_name, sheet_name, filename)


if __name__ == '__main__':
    main()
