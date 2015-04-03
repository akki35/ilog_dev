# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='myuser',
            field=models.ForeignKey(to='accounts.MyUser'),
            preserve_default=True,
        ),
    ]
