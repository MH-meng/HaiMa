# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-01-18 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('introduction', models.CharField(max_length=100, verbose_name='引言')),
                ('time', models.DateTimeField(verbose_name='创建实时间')),
                ('author', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': '新闻',
                'db_table': 'News',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.CharField(max_length=32, verbose_name='出发地')),
                ('destination', models.CharField(max_length=32, verbose_name='目的地')),
                ('status', models.IntegerField(choices=[(0, '下线'), (1, '上线')], default=1, verbose_name='状态')),
                ('type', models.CharField(max_length=64, verbose_name='车辆类型')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('time', models.DateTimeField(verbose_name='时间')),
                ('content', models.CharField(max_length=250, verbose_name='货物介绍')),
                ('author', models.CharField(default='海马', max_length=32)),
            ],
            options={
                'verbose_name_plural': '求车',
                'db_table': 'Price',
                'ordering': ['-time'],
            },
        ),
    ]
