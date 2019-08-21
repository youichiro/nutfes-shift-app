from django.contrib import admin
from apps.notification.models import DeviceToken


class DeviceTokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'token')


admin.site.register(DeviceToken, DeviceTokenAdmin)
