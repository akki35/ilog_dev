# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='last_login',
            field=models.DateTimeField(verbose_name='last login', blank=True, null=True),
            preserve_default=True,
        ),
    ]
