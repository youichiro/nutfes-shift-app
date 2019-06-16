from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .forms import UserCreationForm
from .models import User, Belong, Department, Grade, Member


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


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', )


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('name', 'email', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('name', 'email', 'is_staff')
    ordering = ('name',)


admin.site.register(Belong, BelongAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(User, MyUserAdmin)
