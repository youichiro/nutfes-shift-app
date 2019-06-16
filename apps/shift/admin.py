from django.contrib import admin
from .models import Sheet, Place, Time, Task, Cell


class SheetAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'is_active')
    ordering = ('id',)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    ordering = ('id',)
    list_editable = ('color',)


class TimeAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'is_now')
    ordering = ('id',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'color', 'description')
    ordering = ('id',)
    list_editable = ('color',)


class CellAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'sheet', 'member', 'time', 'task')
    ordering = ('id',)
    list_filter = ('sheet', 'time', 'task')
    search_fields = ('member__name',)


admin.site.register(Sheet, SheetAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Cell, CellAdmin)
