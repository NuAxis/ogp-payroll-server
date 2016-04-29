# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payrolls', '0002_auto_20160419_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='state',
        ),
        migrations.AddField(
            model_name='payrollline',
            name='time_type',
            field=models.TextField(default='REG'),
        ),
        migrations.AddField(
            model_name='worker',
            name='special',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='payrollline',
            name='dol_rate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wage_determinations.Rate'),
        ),
    ]
