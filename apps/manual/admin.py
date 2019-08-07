from django.contrib import admin
from .models import Manual


class ManualAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'order')
    ordering = ('id',)
    list_editable = ('order',)


admin.site.register(Manual, ManualAdmin)
