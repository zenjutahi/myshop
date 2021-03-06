# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeriesList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('seriesSize', models.CharField(db_index=True, max_length=200)),
                ('bookPosition', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=50, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=100),
        ),
    ]
