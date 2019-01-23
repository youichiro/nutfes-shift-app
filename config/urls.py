from django.contrib import admin
from django.urls import path, include
from apps.api.urls import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('apps.account.urls')),
    path('api/', include(router.urls)),
]
