from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'created_date')
    date_hierarchy = 'created_date'
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ("Personal Dates", {'fields': ('first_name', 'last_name', 'avatar',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ("Important Dates", {'fields': ('last_login', 'modified_date', 'created_date')}),
    )
    readonly_fields = ('last_login', 'modified_date', 'created_date')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'is_superuser',)
    filter_horizontal = ('groups', 'user_permissions')
    list_editable = ('is_staff', 'is_active', 'is_superuser')
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    ordering = ()

