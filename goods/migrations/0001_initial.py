# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-17 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=64)),
                ('sity', models.CharField(max_length=64)),
                ('district', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('street', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('house', models.CharField(blank=True, default=None, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('short_description', models.TextField(blank=True, default=None, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категория товаров',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категория товаров',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='goods_img/')),
                ('is_main', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('goods', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Goods')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory'),
        ),
    ]
