from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .forms import UserCreationForm
from .models import User


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
        ('Personal info', {'fields': ('name', 'belong', 'department', 'grade', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('student_id', 'name', 'belong', 'department', 'grade', 'phone_number', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('student_id', 'name', 'belong', 'department', 'grade', 'phone_number', 'is_staff')
    list_filter = ('is_staff', 'belong')
    search_fields = ('name', )
    ordering = ('belong', )


admin.site.register(User, MyUserAdmin)
