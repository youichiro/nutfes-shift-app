import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from apps.notification.models import DeviceToken


@csrf_exempt
def register(request):
    if request.method == 'POST':
        body = request.body
        if type(body) is bytes:
            body = body.decode()
        if type(body) is str:
            body = json.loads(body)
        try:
            token = body['token']
            username = body['username']
            DeviceToken.objects.update_or_create(
                token=token,
                defaults={
                    'token': token,
                    'username': username
                }
            )
            return HttpResponse(f'Saved DeviceToken: {username} {token}')
        except KeyError:
            return HttpResponse('Bad request')
    else:
        return HttpResponse('Bad request')
