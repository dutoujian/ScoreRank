# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('client_name', models.CharField(verbose_name='客户端名称', max_length=150)),
                ('score', models.IntegerField(verbose_name='分数')),
                ('create_time', models.DateTimeField(verbose_name='创建时间')),
                ('update_time', models.DateTimeField(verbose_name='更新时间')),
                ('is_valid', models.CharField(verbose_name='是否有效', max_length=1)),
            ],
            options={
                'db_table': 'client_score',
                'verbose_name': '分数信息',
                'verbose_name_plural': '分数信息',
            },
        ),
    ]
