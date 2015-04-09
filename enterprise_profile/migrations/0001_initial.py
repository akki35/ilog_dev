# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnterpriseProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('address', models.CharField(null=True, blank=True, max_length=200)),
                ('contact', models.CharField(null=True, blank=True, max_length=30)),
                ('website', models.URLField(null=True, blank=True, max_length=255)),
                ('about', models.TextField(blank=True, null=True)),
                ('capabilities', models.TextField(blank=True, null=True)),
                ('people_detail', models.TextField(blank=True, null=True)),
                ('product_intro', models.TextField(blank=True, null=True)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='enterprise/main')),
                ('image_thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='enterprise/thumbnails')),
                ('enterprise', models.OneToOneField(to='enterprise.Enterprise')),
            ],
        ),
    ]
