# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('category', models.CharField(choices=[('F', 'Feed'), ('A', 'Article'), ('C', 'Comment')], default='F', max_length=1)),
                ('title', models.TextField(db_index=True, null=True, blank=True, max_length=255)),
                ('post', models.TextField()),
                ('slug', models.SlugField(null=True, blank=True, max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('score', models.FloatField(default=0)),
                ('myuser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, to='nodes.Node', blank=True)),
            ],
            options={
                'ordering': ('-score', '-date'),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tag', models.CharField(max_length=50)),
                ('article', models.ForeignKey(to='nodes.Node')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('tag', 'article')]),
        ),
        migrations.AlterIndexTogether(
            name='tag',
            index_together=set([('tag', 'article')]),
        ),
    ]
