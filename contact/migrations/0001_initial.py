# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-27 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=20)),
                ('Twiiter', models.CharField(max_length=20)),
                ('Github', models.CharField(max_length=20)),
            ],
        ),
    ]
