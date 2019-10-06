import json
from apps.shift.models import Member


def create_member_json(filename='static/json/members.json', return_json=False):
    """Memberの全データをソートして辞書orJSONで返す"""
    data = []
    for member in Member.objects.all().order_by('belong__id', '-is_leader', '-is_subleader', 'grade__id'):
        data.append({
            'name': member.name,
            'belong_category': member.belong.category_name,
            'belong_subcategory': member.belong.subcategory_name,
            'belong_shortname': member.belong.short_name,
            'color': member.belong.color,
            'grade': member.grade.name,
            'is_leader': member.is_leader,
            'is_subleader': member.is_subleader,
        })

    if return_json:
        return data

    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    filename = 'static/json/members.json'
    print(f'Saving members data to {filename}...')
    create_member_json(filename=filename)
