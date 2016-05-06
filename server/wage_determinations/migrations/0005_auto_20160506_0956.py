# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 09:56
from __future__ import unicode_literals

from django.db import migrations, models
import pg_fts.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wage_determinations', '0004_state_abbrev'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='name',
            field=models.TextField(db_index=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='fts_index',
            field=pg_fts.fields.TSVectorField(default='', dictionary='english', editable=False, fields=(('occupation', 'A'), ('rate_name', 'B'), ('subrate_name', 'B'), 'occupation_qualifier', 'rate_name_qualifier', 'subrate_name_qualifier'), null=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='state',
            name='abbrev',
            field=models.TextField(db_index=True, unique=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.TextField(db_index=True, unique=True),
        ),
    ]
