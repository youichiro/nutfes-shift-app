from django.urls import path
from .views import get_shift_data_json


urlpatterns = [
    path('data/<int:sheet_id>', get_shift_data_json, name='shift_data')
]
