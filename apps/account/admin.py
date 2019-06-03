from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .forms import UserCreationForm
from .models import User, Belong, Department, Grade


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


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('student_id', )


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('student_id', 'password')}),
        ('Personal info', {'fields': ('name', 'belong', 'department', 'grade',
                                      'is_leader', 'is_subleader', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('student_id', 'name', 'belong', 'department', 'grade',
                       'is_leader', 'is_subleader', 'phone_number', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('name', 'belong', 'department', 'grade',
                    'is_leader', 'is_subleader', 'student_id', 'phone_number', 'is_staff')
    list_filter = ('belong', 'grade')
    search_fields = ('name', 'belong__name')
    ordering = ('belong', )


admin.site.register(Belong, BelongAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(User, MyUserAdmin)
