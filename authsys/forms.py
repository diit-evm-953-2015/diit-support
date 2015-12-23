#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model 
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

User = get_user_model()

class UserCreationForm(UserCreationForm):
    error_css_class = 'class-error1'
    class Meta:
        model = get_user_model()
        fields = ("username",'email')
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        #self.fields['email'].help_text = ''
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        for field in self.fields:
                self.fields[field].widget.attrs['class'] = "form-control form_marg"


class AddUserInfo(forms.ModelForm):

    error_css_class = "class-error1"
    class Meta:
        model = get_user_model()
        fields = ('last_name','first_name','middle_name','faculty','department',)
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        # adding css classes to widgets without define the fields:
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control form_marg"


# Допиливаем форму добавления пользователя. В Meta.model указываем нашу модель.
# Поля указывать нет необходимости т.к. они переопределяются в UserAdmin.add_fieldsets 
class AdminUserAddForm(UserCreationForm):
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


# Допиливаем форму редактирования пользователя. В Meta.model указываем нашу модель.
class AdminUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = "__all__"