# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.BooleanField()),
                ('id_cliente', models.AutoField(serialize=False, primary_key=True)),
                ('id_authy', models.CharField(max_length=15)),
                ('area_code', models.CharField(max_length=15)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('nombre', models.CharField(max_length=40)),
                ('apaterno', models.CharField(max_length=25)),
                ('amaterno', models.CharField(max_length=25)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=22)),
                ('email', models.CharField(unique=True, max_length=30)),
                ('genero', models.TextField()),
                ('identificacion', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(null=True, blank=True)),
                ('red_social', models.TextField()),
                ('avatar', models.CharField(max_length=100)),
                ('is_active', models.BooleanField()),
                ('is_staff', models.BooleanField()),
            ],
            options={
                'db_table': 'users_user',
                'managed': False,
            },
        ),
    ]
