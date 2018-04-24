# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-24 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldmap', '0005_auto_20180423_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendSMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_number', models.CharField(max_length=30)),
                ('from_number', models.CharField(max_length=30)),
                ('body', models.CharField(blank=True, default='', max_length=500)),
                ('sms_sid', models.CharField(blank=True, default='', max_length=34)),
                ('account_sid', models.CharField(blank=True, default='', max_length=34)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sent_at', models.DateTimeField(blank=True, null=True)),
                ('delivered_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, default='', max_length=20)),
            ],
        ),
    ]
