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
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('message', models.TextField(max_length=5000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('conversation', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('from_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('myuser', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
            options={
                'verbose_name_plural': 'Messages',
                'ordering': ('date',),
                'verbose_name': 'Message',
            },
            bases=(models.Model,),
        ),
    ]
