#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from authsys.models import *
from formtools.wizard.views import SessionWizardView
from authsys.forms import AddUserInfo,UserCreationForm
from django.contrib import auth
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

FORMS = [("login_pass", UserCreationForm),
         ("user_info", AddUserInfo)]

TEMPLATES = {"login_pass": "authsys/reg_login_pass.html",
             "user_info": "authsys/reg_user_info.html"}


class RegistrationWizard(SessionWizardView):

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    file_storage = FileSystemStorage('avatars')

    def done(self, form_list, **kwargs):
    	user = User()
    	user.username = form_list[0].cleaned_data['username']
    	password = form_list[0].cleaned_data['password2']
        user.set_password(password)
    	user.last_name = form_list[1].cleaned_data['last_name']
        user.email = form_list[0].cleaned_data['email']
    	user.first_name = form_list[1].cleaned_data['first_name']
    	user.middle_name = form_list[1].cleaned_data['middle_name']
    	user.faculty = form_list[1].cleaned_data['faculty']
    	user.department = form_list[1].cleaned_data['department']
        #user.av = self.file_storage.url('avatar')
    	#user.group = form_list[1].cleaned_data['group']
    	user.save()
        #return render_to_response('authsys/done.html',)
        return HttpResponseRedirect('/',)

def profiles(request,):
    #user = auth.get_user(request)
    user_list = User.objects.all()
    return render(request, 'authsys/profiles.html',{'user_list':user_list} )

def profile(request,user_id=1):
    #user = auth.get_user(request)
    user_profile = get_object_or_404(User, pk=user_id)
    context = {'full_name': user_profile.get_full_name(),
                'faculty':user_profile.faculty,
                'department':user_profile.department,
                'username':user_profile.username,
                'avatar':user_profile.avatar,
                'id':user_profile.id,
               }
    return render(request, 'authsys/profile.html',context,)


def login(request):
    if request.user.is_active:
        return HttpResponseRedirect("profiles")
    if request.POST :
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Правильный пароль и пользователь "активен"
            auth.login(request, user)
            # Перенаправление на "правильную" страницу
            return HttpResponseRedirect("/profiles")
        else:
            # Отображение страницы с ошибкой
            login_error = "Не удается войти. Проверьте логин и пароль" 
            return render(request, 'authsys/login.html',{'login_error':login_error})
    else:
        return render(request, 'authsys/login.html',)


def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("login")


def thanks(request):
    return render(request, 'authsys/thanks.html')


def about(request):
    return render(request, 'authsys/about.html')

