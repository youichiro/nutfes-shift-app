from django.contrib import admin
from apps.notification.models import DeviceToken


class DeviceTokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'token', 'created_at', 'updated_at')


admin.site.register(DeviceToken, DeviceTokenAdmin)
