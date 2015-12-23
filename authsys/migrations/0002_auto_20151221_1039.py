# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(max_length=1000, upload_to=b'avatars/', null=True, verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440', blank=True),
        ),
    ]
