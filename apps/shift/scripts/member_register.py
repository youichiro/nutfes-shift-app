import openpyxl
from django.conf import settings
from apps.shift.models import Belong, Department, Grade, Member

# 技大祭名簿excelファイルの情報を定義する
FILENAME = 'members.xlsx'
CATEGORY_RANGE = 'B2:B152'
SUBCATEGORY_RANGE = 'C2:C152'
LEADER_RANGE = 'D2:D152'
GRADE_RANGE = 'E2:E152'
DEPARTMENT_RANGE = 'F2:F152'
NAME_RANGE = 'G2:G152'
EMAIL_RANGE = 'I2:I152'
PHONE_RANGE = 'K2:K152'


def get_value_list(tuple_2d):
    """セルオブジェクトの2次元配列からセルの値の2次元配列に変換する"""
    return [[cell.value for cell in row] for row in tuple_2d]


def main():
    """技大祭名簿excelを読み取ってデータベースに保存する"""
    member_file = settings.BASE_DIR + '/static/xlsx/' + FILENAME
    member_wb = openpyxl.load_workbook(member_file)
    member_sheet = member_wb.active

    # 局を取得
    category_values = member_sheet[CATEGORY_RANGE]
    category_values = get_value_list(category_values)

    # 部門を取得
    subcategory_values = member_sheet[SUBCATEGORY_RANGE]
    subcategory_values = get_value_list(subcategory_values)

    # 部門長かどうかを取得
    is_leader_values = member_sheet[LEADER_RANGE]
    is_leader_values = get_value_list(is_leader_values)

    # 学年を取得
    grade_values = member_sheet[GRADE_RANGE]
    grade_values = get_value_list(grade_values)

    # 学科を取得
    department_values = member_sheet[DEPARTMENT_RANGE]
    department_values = get_value_list(department_values)

    # 名前を取得
    name_values = member_sheet[NAME_RANGE]
    name_values = get_value_list(name_values)

    # メールアドレスを取得
    email_values = member_sheet[EMAIL_RANGE]
    email_values = get_value_list(email_values)

    phone_values = member_sheet[PHONE_RANGE]
    phone_values = get_value_list(phone_values)

    for category, subcategory, is_leader, grade, department, name, email, phone \
            in zip(category_values, subcategory_values, is_leader_values, grade_values,
                   department_values, name_values, email_values, phone_values):
        if not name[0]:
            continue
        name = name[0].replace(' ', '').replace('　', '')  # 名前の空白を削除
        email = email[0]
        phone_number = str(phone[0]) if phone[0] else None
        subcategory = None if subcategory[0] == '-' else subcategory[0]
        belong = Belong.objects.filter(category_name=category[0], subcategory_name=subcategory).first()
        department = Department.objects.filter(name=department[0] or '未所属').first()
        grade = Grade.objects.filter(name=grade[0]).first()
        is_leader = True if (is_leader[0] == '部門長' or
                             subcategory == '局長' or
                             category[0] == '委員長' or
                             category[0] == '副委員長') else False
        is_subleader = True if subcategory == '副局長' else False
        assert belong is not None and department is not None and grade is not None

        member = Member.objects.filter(name=name).first()
        if member:
            member.belong = belong
            member.department = department
            member.grade = grade
            member.is_leader = is_leader
            member.is_subleader = is_subleader
            member.email = email
            member.phone_number = phone_number
            member.save()
        else:
            Member.objects.create(name=name,
                                  belong=belong,
                                  department=department,
                                  grade=grade,
                                  is_leader=is_leader,
                                  is_subleader=is_subleader,
                                  email=email,
                                  phone_number=phone_number)

    print("Finished saving members")
