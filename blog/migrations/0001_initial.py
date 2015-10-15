# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=10000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
