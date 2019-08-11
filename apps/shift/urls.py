from django.urls import path
from .views import shift_data_json, same_time_members_json


urlpatterns = [
    path('api/<int:sheet_id>', shift_data_json, name='shift_data_api'),
    path('api/members/<str:sheet_name>/<str:task_name>/<int:start_time_id>/<int:end_time_id>', same_time_members_json,
         name='same_time_members_api'),
]
