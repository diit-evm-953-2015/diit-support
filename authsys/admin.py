#!/usr/bin/python
# -*- coding: utf-8 -*-
from authsys.forms import AdminUserChangeForm, AdminUserAddForm
from authsys.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _


# Указываем наши форма для создания и редактирования пользователя.
# Добавляем новые поля в fieldsets, и поле email в add_fieldsets.
class UserAdmin(BaseUserAdmin):
    form = AdminUserChangeForm
    add_form = AdminUserAddForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
        	'last_name',
            'first_name',
            'middle_name',
            'email',
            'avatar',
            'date_of_birth',
            'faculty',
            'department',
            'group'
        )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Department)
admin.site.register(Faculty)
