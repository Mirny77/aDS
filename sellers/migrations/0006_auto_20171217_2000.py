# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-17 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0005_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус продавца', 'verbose_name_plural': 'Статусы продавца'},
        ),
        migrations.AddField(
            model_name='seller',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sellers.Status'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(blank=True, default=1, max_length=24, null=True),
        ),
    ]
