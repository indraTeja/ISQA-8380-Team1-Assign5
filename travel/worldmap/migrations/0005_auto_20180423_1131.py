# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-23 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldmap', '0004_auto_20180423_1112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitorinterest',
            old_name='name',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='visitorinterest',
            name='locationName',
        ),
        migrations.AlterField(
            model_name='visitorinterest',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]