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
            name='EnterpriseAsset',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('product_image', imagekit.models.fields.ProcessedImageField(upload_to='assets/main')),
                ('product_image_thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='assets/thumbnails')),
                ('caption', models.CharField(default='product', max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=True)),
                ('asset', models.ForeignKey(to='enterprise.Asset')),
                ('enterprise', models.ForeignKey(to='enterprise.Enterprise')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='assets',
            field=models.ManyToManyField(to='enterprise.Asset', through='enterprise.EnterpriseAsset'),
            preserve_default=True,
        ),
    ]
