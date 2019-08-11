from django.urls import path
from .views import shift_data_json, same_time_members_json, is_nutfes_email


urlpatterns = [
    path('api/<int:sheet_id>', shift_data_json, name='shift_data_api'),
    path('api/members/<str:sheet_name>/<str:task_name>/<int:start_time_id>/<int:end_time_id>', same_time_members_json,
         name='same_time_members_api'),
    path('api/check_email/<str:email>', is_nutfes_email, name='check_email'),
]
