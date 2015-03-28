# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])),
                ('job_position', models.CharField(max_length=255)),
                ('experience', models.TextField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('score', models.FloatField(default=0)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='user/main')),
                ('image_thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='user/thumbnails')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('status', models.CharField(max_length=1, choices=[('F', 'Following'), ('B', 'Blocked')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(related_name='from_person', to='myuserprofile.MyUserProfile')),
                ('to_user', models.ForeignKey(related_name='to_person', to='myuserprofile.MyUserProfile')),
            ],
            options={
                'verbose_name_plural': 'relationships',
                'ordering': ('created',),
                'verbose_name': 'relationship',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='myuserprofile',
            name='follows',
            field=models.ManyToManyField(to='myuserprofile.MyUserProfile', related_name='related_to', through='myuserprofile.Relationship'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuserprofile',
            name='myuser',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuserprofile',
            name='skillset',
            field=models.ManyToManyField(to='enterprise.Operation'),
            preserve_default=True,
        ),
    ]
