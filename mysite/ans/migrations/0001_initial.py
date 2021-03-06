# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('pub_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('pub_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Upvotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('answers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ans.Answers')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='upvotes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ans.User'),
        ),
        migrations.AddField(
            model_name='questions',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ans.User'),
        ),
        migrations.AddField(
            model_name='answers',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ans.Questions'),
        ),
        migrations.AddField(
            model_name='answers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ans.User'),
        ),
    ]
