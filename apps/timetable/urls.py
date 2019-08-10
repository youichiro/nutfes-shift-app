from django.urls import path
from .views import timetable_json


urlpatterns = [
    path('api/', timetable_json, name='timetable_api')
]
