# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterpriseprofile',
            name='capabilities',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enterpriseprofile',
            name='people_detail',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enterpriseprofile',
            name='product_intro',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
