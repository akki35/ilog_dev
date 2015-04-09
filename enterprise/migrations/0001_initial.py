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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Asset',
            },
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('enterprise', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('allassets', models.ManyToManyField(to='enterprise.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='EnterpriseAsset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('asset_image', imagekit.models.fields.ProcessedImageField(upload_to='assets/main')),
                ('asset_image_thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='assets/thumbnails')),
                ('caption', models.CharField(default='product', max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=True)),
                ('asset', models.ForeignKey(to='enterprise.Asset')),
                ('enterprise', models.ForeignKey(to='enterprise.Enterprise')),
            ],
        ),
        migrations.CreateModel(
            name='EnterpriseProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('product_image', imagekit.models.fields.ProcessedImageField(upload_to='products/main')),
                ('product_image_thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='products/thumbnails')),
                ('caption', models.CharField(default='product', max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=True)),
                ('enterprise', models.ForeignKey(to='enterprise.Enterprise')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Material',
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'operation',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Type',
            },
        ),
        migrations.AddField(
            model_name='enterpriseproduct',
            name='product',
            field=models.ForeignKey(to='enterprise.Product'),
        ),
        migrations.AddField(
            model_name='enterprise',
            name='materials',
            field=models.ManyToManyField(to='enterprise.Material'),
        ),
        migrations.AddField(
            model_name='enterprise',
            name='operations',
            field=models.ManyToManyField(to='enterprise.Operation'),
        ),
        migrations.AddField(
            model_name='enterprise',
            name='products',
            field=models.ManyToManyField(through='enterprise.EnterpriseProduct', to='enterprise.Product'),
        ),
        migrations.AddField(
            model_name='enterprise',
            name='types',
            field=models.ManyToManyField(to='enterprise.Type'),
        ),
    ]
