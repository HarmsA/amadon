# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-09 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20181209_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]