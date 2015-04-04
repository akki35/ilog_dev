# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150403_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='last_login',
            field=models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
