# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-26 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0004_auto_20180306_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='contact',
            field=models.CharField(max_length=17),
        ),
    ]