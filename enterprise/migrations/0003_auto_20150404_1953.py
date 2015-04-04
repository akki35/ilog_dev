# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0002_auto_20150404_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enterpriseasset',
            old_name='product_image',
            new_name='asset_image',
        ),
        migrations.RenameField(
            model_name='enterpriseasset',
            old_name='product_image_thumbnail',
            new_name='asset_image_thumbnail',
        ),
    ]
