# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=15)),
                ('temp_pass', models.CharField(max_length=122, blank=True)),
                ('activation_key', models.CharField(max_length=40, blank=True)),
                ('key_expires', models.DateTimeField(default=datetime.date(2016, 3, 23))),
                ('email', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=False)),
                ('status', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'User profiles',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
    ]
