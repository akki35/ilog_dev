# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(to='accounts.MyUser', related_name='+'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='from_user',
            field=models.ForeignKey(to='accounts.MyUser', related_name='+'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='myuser',
            field=models.ForeignKey(to='accounts.MyUser', related_name='+'),
            preserve_default=True,
        ),
    ]
