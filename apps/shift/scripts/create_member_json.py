import json
from apps.shift.models import Member


JSON_FILE_PATH = 'static/json/members.json'


def main():
    data = []
    for member in Member.objects.all().order_by('belong__id', '-is_leader', '-is_subleader', '-grade__id'):
        data.append({
            'name': member.name,
            'belong_category': member.belong.category_name,
            'belong_subcategory': member.belong.subcategory_name,
            'belong_shortname': member.belong.short_name,
            'color': member.belong.color,
            'grade': member.grade.name,
            'is_leader': member.is_leader,
            'is_subleader': member.is_subleader,
            'phone_number': member.phone_number,
        })

    with open(JSON_FILE_PATH, 'w') as f:
        json.dump(data, f, ensure_ascii=False)
    print('Saved json file:', JSON_FILE_PATH)
