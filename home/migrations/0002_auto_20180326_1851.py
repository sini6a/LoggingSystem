# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-26 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company_logo',
            field=models.ImageField(blank=True, upload_to='logos/'),
        ),
    ]
