#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Faculty(models.Model):
    title = models.CharField(_(u'Абревиатура факультет'),default='', max_length=5, )
    full_name = models.CharField(_(u'Название факультета'),default='', max_length=100, )
    def __unicode__(self):
        return self.title

    #def select_department(self):
    #	return Department.objects.get(pk=1)

class Department(models.Model):
    title = models.CharField(_(u'Абревиатура кафедры'),default='', max_length=10, )
    full_name = models.CharField(_(u'Название кафедры'),default='',max_length=100, )
    faculty = models.ForeignKey( Faculty, verbose_name=_(u'Факультет'),null=True,  )
    
    def __unicode__(self):
        return self.title

class User(AbstractUser):
    avatar = models.ImageField(_(u'Аватар'), blank=True, null=True, upload_to="avatars", default="avatars/blank-avatar.png", max_length=1000)
    middle_name = models.CharField(_(u'Отчество'), max_length=40, null=True, blank=True)
    date_of_birth = models.DateField(_(u'Дата рождения'), null=True, blank=True)
    faculty = models.ForeignKey(Faculty, verbose_name=_(u'Факультет'), null=True, ) 
    department =  models.ForeignKey (Department, verbose_name=_(u'Кафедра'), null=True,)
    group = models.CharField(_('group'),default='',  max_length=10,blank=True )

    def get_full_name(self):
        """
        Returns the first_name plus the last_name plus middle_name, with a space in between.
        """
        full_name = '%s %s %s' % (self.last_name, self.first_name, self.middle_name )
        return full_name.strip()
    
    def get_short_name(self):
        short_name = '%s %s ' % (self.first_name, self.last_name )
        return short_name

    
    class Meta:
        ordering = ['last_name']
        verbose_name = _(u'Пользователь')
        verbose_name_plural = _(u'Пользователи')