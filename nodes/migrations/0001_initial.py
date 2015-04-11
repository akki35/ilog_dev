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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('category', models.CharField(default='F', choices=[('F', 'Feed'), ('A', 'Article'), ('C', 'Comment')], max_length=1)),
                ('title', models.TextField(db_index=True, blank=True, max_length=255, null=True)),
                ('post', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('score', models.FloatField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('myuser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, to='nodes.Node')),
            ],
            options={
                'ordering': ('-score', '-date'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tag', models.CharField(max_length=50)),
                ('article', models.ForeignKey(to='nodes.Node')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
            bases=(models.Model,),
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
