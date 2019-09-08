from django.urls import path
from .views import (
    shift_data_json, same_time_members_json, is_nutfes_email, members_json,
    my_shift_data_json, task_shift_data_json
)


app_name = 'shift'
urlpatterns = [
    path('api/<int:sheet_id>', shift_data_json, name='shift_data_api'),
    path('api/members/<str:sheet_name>/<str:task_name>/<int:start_time_id>/<int:end_time_id>', same_time_members_json,
         name='same_time_members_api'),
    path('api/check_email/<str:email>', is_nutfes_email, name='check_email'),
    path('api/member_list', members_json, name='member_list'),
    path('api/my_shift/<str:member_name>', my_shift_data_json, name='my_shift_data_api'),
    path('api/task_shift/<int:sheet_id>/<str:task_name>', task_shift_data_json, name='task_shift_data_api'),
]
