# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0002_auto_20151221_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(max_length=1000, upload_to=b'authsys/static/authsys/media/avatars', null=True, verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440', blank=True),
        ),
    ]
