# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scorerank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinfo',
            name='is_valid',
            field=models.CharField(default=1, max_length=1, verbose_name='是否有效'),
        ),
    ]
