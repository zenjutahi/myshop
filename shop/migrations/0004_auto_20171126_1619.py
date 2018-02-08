# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20171120_1046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-updated', '-created')},
        ),
        migrations.AlterField(
            model_name='serieslist',
            name='bookPosition',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
