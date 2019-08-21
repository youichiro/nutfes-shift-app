from django.urls import path
from .views import register


app_name = 'notification'
urlpatterns = [
    path('registration', register, name='device_token_registration'),
]
