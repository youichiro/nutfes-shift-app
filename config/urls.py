from django.contrib import admin
from django.urls import path, include
from apps.api.urls import router
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('apps.account.urls')),
    path('api/', include(router.urls)),
    path('shift/', include('apps.shift.urls')),
    path('timetable/', include('apps.timetable.urls')),
    path('option/', include('apps.option.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
