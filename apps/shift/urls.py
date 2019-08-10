from django.urls import path
from .views import shift_data_json


urlpatterns = [
    path('api/<int:sheet_id>', shift_data_json, name='shift_data_api')
]
