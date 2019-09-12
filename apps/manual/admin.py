from django.contrib import admin
from .models import Manual


class ManualAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'url', 'order')
    ordering = ('id',)
    list_editable = ('url', 'order')


admin.site.register(Manual, ManualAdmin)
