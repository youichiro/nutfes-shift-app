from django.contrib import admin
from .models import TimeTable, Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color')
    ordering = ('id',)
    list_editable = ('color',)


class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'sheet_name', 'place', 'start_time', 'end_time', 'event')
    ordering = ('id',)


admin.site.register(Event, EventAdmin)
admin.site.register(TimeTable, TimeTableAdmin)
