from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.api.urls import router
from django.views.generic import TemplateView


admin.site.site_title = 'nutfes-shift-app'
admin.site.site_header = 'NUTFES SHIFT APP'


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('account/', include('apps.account.urls')),
    path('api/', include(router.urls)),
    path('shift/', include('apps.shift.urls')),
    path('timetable/', include('apps.timetable.urls')),
    path('option/', include('apps.option.urls')),
    path('notification/', include('apps.notification.urls')),
    path('contact/', include('apps.contact.urls')),
    path('markdownx/', include('markdownx.urls')),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
