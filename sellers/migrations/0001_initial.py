# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-17 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0004_auto_20171217_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(default=None, max_length=64, null=True)),
                ('status', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods')),
            ],
            options={
                'verbose_name': 'Продавец',
                'verbose_name_plural': 'Продавцы',
            },
        ),
    ]
