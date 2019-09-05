from django.urls import path
from .views import register, NotificationFormView


app_name = 'notification'
urlpatterns = [
    path('registration', register, name='device_token_registration'),
    path('form', NotificationFormView.as_view(), name='form'),
]
