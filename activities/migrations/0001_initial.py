# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nodes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('activity', models.CharField(max_length=1, choices=[('L', 'Like')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('node', models.IntegerField(null=True, blank=True)),
                ('myuser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Activities',
                'verbose_name': 'Activity',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('notification_type', models.CharField(max_length=1, choices=[('L', 'Liked'), ('C', 'Commented'), ('S', 'Also commented'), ('K', 'Also joined'), ('E', 'Edited'), ('F', 'Follows')])),
                ('is_read', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('node', models.ForeignKey(to='nodes.Node')),
                ('to_user', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Notifications',
                'verbose_name': 'Notification',
                'ordering': ('-date',),
            },
            bases=(models.Model,),
        ),
    ]
