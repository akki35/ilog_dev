# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enterprise',
            name='allassets',
        ),
        migrations.AddField(
            model_name='enterprise',
            name='assets',
            field=models.ManyToManyField(through='enterprise.EnterpriseAsset', to='enterprise.Asset'),
        ),
    ]
