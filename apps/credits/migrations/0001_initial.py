# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id_credito', models.AutoField(serialize=False, primary_key=True)),
                ('monto', models.FloatField()),
                ('interes', models.FloatField()),
                ('t_interes', models.FloatField()),
                ('fecha_in', models.DateTimeField()),
                ('fecha_fin', models.DateField()),
                ('fecha_real', models.DateField(null=True, blank=True)),
                ('ponderacion', models.TextField()),
                ('status', models.IntegerField()),
                ('plazo', models.IntegerField()),
                ('total', models.FloatField()),
                ('pago_diario', models.FloatField(null=True, blank=True)),
                ('lista_dias', models.CharField(max_length=900, null=True, blank=True)),
            ],
            options={
                'db_table': 'credits_credit',
                'managed': False,
            },
        ),
    ]
