# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-08-07 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20190714_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountentry',
            name='advance',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='accountentry',
            name='balance',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='accountentry',
            name='freight',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='accountentry',
            name='hamali',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='accountentry',
            name='netcollection',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='accountentry',
            name='paid_balance',
            field=models.FloatField(),
        ),
    ]
