# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.core.validators
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(max_length=1000, upload_to=b'user/avatar', null=True, verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440', blank=True)),
                ('middle_name', models.CharField(max_length=40, null=True, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e', blank=True)),
                ('date_of_birth', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f', blank=True)),
                ('group', models.CharField(default=b'', max_length=10, verbose_name='group')),
            ],
            options={
                'verbose_name': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=10, verbose_name='\u0410\u0431\u0440\u0435\u0432\u0438\u0430\u0442\u0443\u0440\u0430 \u043a\u0430\u0444\u0435\u0434\u0440\u044b')),
                ('full_name', models.CharField(default=b'', max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0444\u0435\u0434\u0440\u044b')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=5, verbose_name='\u0410\u0431\u0440\u0435\u0432\u0438\u0430\u0442\u0443\u0440\u0430 \u0444\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442')),
                ('full_name', models.CharField(default=b'', max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442\u0430')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(verbose_name='\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442', to='authsys.Faculty', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(verbose_name='\u041a\u0430\u0444\u0435\u0434\u0440\u0430', to='authsys.Department', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='faculty',
            field=models.ForeignKey(verbose_name='\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442', to='authsys.Faculty', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
    ]
