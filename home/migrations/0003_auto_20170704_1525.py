# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_pool_number_of_teams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.CharField(default='0', max_length=1),
        ),
    ]