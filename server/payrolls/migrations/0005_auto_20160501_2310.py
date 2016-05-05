# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 23:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payrolls', '0004_payrollupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='job_name',
            field=models.TextField(default='unknown'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.TextField(default='MN'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='day',
            name='work_classification',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wage_determinations.County'),
        ),
    ]