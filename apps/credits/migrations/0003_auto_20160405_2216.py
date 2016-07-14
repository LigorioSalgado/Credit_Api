# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('credits', '0002_auto_20160324_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='cuenta',
            field=models.ForeignKey(related_name='Account', to='accounts.Account', null=True),
        ),
        migrations.AlterModelTable(
            name='credit',
            table=None,
        ),
    ]
