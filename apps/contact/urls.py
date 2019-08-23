from django.urls import path
from .views import contact_json, contact_view


app_name = 'contact'
urlpatterns = [
    path('api/', contact_json, name='contact_api'),
    path('<int:contact_id>', contact_view, name='contact'),
]
