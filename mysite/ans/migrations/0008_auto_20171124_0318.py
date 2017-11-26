# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 21:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ans', '0007_auto_20171124_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ans.UserInfo'),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ans.UserInfo'),
        ),
    ]
