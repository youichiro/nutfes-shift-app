from django.contrib import admin
from .models import Belong, Department, Grade, Member, Sheet, Time, Task, Cell


class BelongAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'color', 'order')
    ordering = ('order',)
    list_editable = ('color',)  # 一覧ページで編集できる


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('id',)


class GradeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ('order',)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'student_id', 'belong', 'department', 'grade', 'is_leader', 'is_subleader')
    ordering = ('belong__order',)


class SheetAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'is_active')
    ordering = ('id',)


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


admin.site.register(Belong, BelongAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Sheet, SheetAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Cell, CellAdmin)
