from django.urls import path
from .views import weather_json


urlpatterns = [
    path('api/weather/', weather_json, name='weather_api'),
]
