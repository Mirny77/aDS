# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-17 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0006_auto_20171217_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=24, null=True),
        ),
    ]