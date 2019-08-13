from django.contrib import admin
from .models import Option


class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'weather', 'api_mode')


admin.site.register(Option, OptionAdmin)
