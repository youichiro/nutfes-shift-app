import json
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from apps.notification.models import DeviceToken
from apps.notification.scripts.send_notifications import send_notification
from apps.notification.forms import NotificationForm


@csrf_exempt
def register(request):
    """POSTされたデバイストークンを受け取って保存する"""
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


class NotificationFormView(LoginRequiredMixin, FormView):
    login_url = '/admin/login/'
    template_name = 'notification/notification_form.html'
    form_class = NotificationForm

    def form_valid(self, form):
        title = form.cleaned_data['title']
        body = form.cleaned_data['body']
        send_notification(title, body)
        messages.info(self.request, '通知を送信しました')
        return redirect(reverse_lazy('notification:form'))
