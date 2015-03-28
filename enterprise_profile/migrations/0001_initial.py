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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('address', models.CharField(blank=True, null=True, max_length=200)),
                ('contact', models.CharField(blank=True, null=True, max_length=30)),
                ('website', models.URLField(blank=True, null=True, max_length=255)),
                ('about', models.TextField(null=True, blank=True)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='enterprise/main')),
                ('image_thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='enterprise/thumbnails')),
                ('enterprise', models.OneToOneField(to='enterprise.Enterprise')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
