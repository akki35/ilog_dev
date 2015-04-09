# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enterprise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('job_position', models.CharField(max_length=255)),
                ('experience', models.TextField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('score', models.FloatField(default=0)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='user/main')),
                ('image_thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='user/thumbnails')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('status', models.CharField(choices=[('F', 'Following'), ('B', 'Blocked')], max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(to='myuserprofile.MyUserProfile', related_name='from_person')),
                ('to_user', models.ForeignKey(to='myuserprofile.MyUserProfile', related_name='to_person')),
            ],
            options={
                'verbose_name': 'relationship',
                'verbose_name_plural': 'relationships',
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='myuserprofile',
            name='follows',
            field=models.ManyToManyField(related_name='related_to', through='myuserprofile.Relationship', to='myuserprofile.MyUserProfile'),
        ),
        migrations.AddField(
            model_name='myuserprofile',
            name='myuser',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='myuserprofile',
            name='skillset',
            field=models.ManyToManyField(to='enterprise.Operation'),
        ),
    ]
