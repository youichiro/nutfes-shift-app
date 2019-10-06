# https://narito.ninja/blog/detail/102/
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from apps.contact.models import Contact


def contact_json(request):
    """APIで返すJSONを作成する"""
    contacts = Contact.objects.all()
    data = []
    for contact in contacts:
        data.append({
            'id': contact.id,
            'title': contact.title,
            'text': contact.html_text(),
            'created_at': contact.created_at.astimezone(tz=None).strftime('%-m月%-d日%H:%M'),
            'updated_at': contact.updated_at.astimezone(tz=None).strftime('%-m月%-d日%H:%M')
        })
    response = json.dumps(data, ensure_ascii=False)
    return JsonResponse(response, safe=False)


@login_required(login_url='/admin/login/')
def contact_view(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'contact/contact.html', {'contact': contact})
