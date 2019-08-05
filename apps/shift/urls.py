from django.urls import path
from .views import create_shift_data_json


urlpatterns = [
    path('api/<int:sheet_id>', create_shift_data_json, name='shift_data_api')
]
