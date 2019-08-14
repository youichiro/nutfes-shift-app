from django.contrib import admin
from .models import Belong, Department, Grade, Member, Sheet, Time, Task, Cell


class BelongAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'short_name', 'color', 'order')
    ordering = ('id',)
    list_editable = ('color',)  # 一覧ページで編集できる


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    ordering = ('id',)


class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order')
    ordering = ('id',)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'belong', 'department', 'grade', 'is_leader', 'is_subleader', 'email', 'phone_number')
    ordering = ('id',)
    search_fields = ('name',)
    list_filter = ('belong__category_name',)


class SheetAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('id',)


class TimeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'start_time', 'end_time')
    ordering = ('id',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'color', 'description')
    ordering = ('id',)
    list_editable = ('color',)
    search_fields = ('name',)


class CellAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'sheet', 'member', 'time', 'task')
    ordering = ('id',)
    list_filter = ('sheet', 'member__belong', 'time')
    search_fields = ('member__name', 'task')


admin.site.register(Belong, BelongAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Sheet, SheetAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Cell, CellAdmin)
