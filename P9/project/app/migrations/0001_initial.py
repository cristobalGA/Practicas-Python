# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido_Paterno', models.CharField(max_length=24)),
                ('Apellido_Materno', models.CharField(max_length=24)),
                ('Edad', models.IntegerField()),
            ],
        ),
    ]
