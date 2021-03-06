# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 13:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='insurance',
            options={'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='insurance',
            name='profile',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='api.Profile'),
            preserve_default=False,
        ),
    ]
