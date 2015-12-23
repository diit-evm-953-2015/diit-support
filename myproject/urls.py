#!/usr/bin/python
# -*- coding: utf-8 -*-
"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from authsys.views import RegistrationWizard, FORMS, profile, profiles,login,logout,about

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^messages/', include('privatemessages.urls')),
    url(r'^authsys/', include('authsys.urls')),
    url(r'^register/$', RegistrationWizard.as_view(FORMS), name='register'),
    url(r'^login$', login, name ='login'),
    url(r'^logout$', logout, name ='logout'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', profile, name='profile'),
    url(r'^profiles/$', profiles, name='profiles'),
    url(r'^about/$', about, name='about'),
    url(r'^$', profiles, name='/'),

]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))