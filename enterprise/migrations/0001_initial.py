# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Asset',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('enterprise', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EnterpriseAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('asset_image', imagekit.models.fields.ProcessedImageField(upload_to='assets/main')),
                ('asset_image_thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='assets/thumbnails')),
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
        migrations.CreateModel(
            name='EnterpriseProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('product_image', imagekit.models.fields.ProcessedImageField(upload_to='products/main')),
                ('product_image_thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='products/thumbnails')),
                ('caption', models.CharField(default='product', max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=True)),
                ('enterprise', models.ForeignKey(to='enterprise.Enterprise')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Material',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'operation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Product',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Type',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='enterpriseproduct',
            name='product',
            field=models.ForeignKey(to='enterprise.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enterprise',
            name='assets',
            field=models.ManyToManyField(through='enterprise.EnterpriseAsset', to='enterprise.Asset'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enterprise',
            name='materials',
            field=models.ManyToManyField(to='enterprise.Material'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enterprise',
            name='operations',
            field=models.ManyToManyField(to='enterprise.Operation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enterprise',
            name='products',
            field=models.ManyToManyField(through='enterprise.EnterpriseProduct', to='enterprise.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enterprise',
            name='types',
            field=models.ManyToManyField(to='enterprise.Type'),
            preserve_default=True,
        ),
    ]
