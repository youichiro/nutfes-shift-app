from django.urls import path
from .views import create_timetable_json


urlpatterns = [
    path('api/', create_timetable_json, name='timetable_api')
]
