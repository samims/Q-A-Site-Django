# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ans', '0003_auto_20171123_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
