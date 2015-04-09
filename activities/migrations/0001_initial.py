# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('activity', models.CharField(choices=[('L', 'Like')], max_length=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('node', models.IntegerField(blank=True, null=True)),
                ('myuser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('notification_type', models.CharField(choices=[('L', 'Liked'), ('C', 'Commented'), ('S', 'Also commented'), ('K', 'Also joined'), ('E', 'Edited'), ('F', 'Follows')], max_length=1)),
                ('is_read', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('node', models.ForeignKey(to='nodes.Node')),
                ('to_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'ordering': ('-date',),
            },
        ),
    ]
