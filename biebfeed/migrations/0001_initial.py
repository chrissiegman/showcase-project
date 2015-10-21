# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='twitter_target',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('target_username', models.CharField(max_length='20')),
                ('user', models.ForeignKey(to='showcase_app.UserProfile')),
            ],
        ),
    ]
