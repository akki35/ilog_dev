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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('address', models.CharField(max_length=200, blank=True, null=True)),
                ('contact', models.CharField(max_length=30, blank=True, null=True)),
                ('website', models.URLField(max_length=255, blank=True, null=True)),
                ('about', models.TextField(null=True, blank=True)),
                ('capabilities', models.TextField(null=True, blank=True)),
                ('people_detail', models.TextField(null=True, blank=True)),
                ('product_intro', models.TextField(null=True, blank=True)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='enterprise/main')),
                ('image_thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='enterprise/thumbnails')),
                ('enterprise', models.OneToOneField(to='enterprise.Enterprise')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
