# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='myuser',
            field=models.ForeignKey(to='accounts.MyUser'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='from_user',
            field=models.ForeignKey(to='accounts.MyUser', related_name='+'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='to_user',
            field=models.ForeignKey(to='accounts.MyUser', related_name='+'),
        ),
    ]
