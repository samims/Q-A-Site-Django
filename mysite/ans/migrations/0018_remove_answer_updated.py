# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-24 08:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ans', '0017_answer_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='updated',
        ),
    ]
