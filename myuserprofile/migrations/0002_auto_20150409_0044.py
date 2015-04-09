# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myuserprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuserprofile',
            name='myuser',
            field=models.OneToOneField(to='accounts.MyUser'),
        ),
    ]
