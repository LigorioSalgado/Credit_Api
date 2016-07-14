# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('no_cuenta', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('historial', models.TextField()),
                ('punt_game', models.IntegerField()),
                ('friend', models.TextField()),
            ],
            options={
                'db_table': 'accounts_account',
                'managed': False,
            },
        ),
    ]
