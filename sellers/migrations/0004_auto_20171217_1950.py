# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-17 16:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0003_auto_20171217_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='status',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]