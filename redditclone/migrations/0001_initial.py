# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
                ('rank_score', models.FloatField(default=0.0)),
                ('url', models.URLField(max_length=250, verbose_name='URL', blank=True)),
                ('description', models.TextField(blank=True)),
                ('submitter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('link', models.ForeignKey(to='redditclone.Link')),
                ('voter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
