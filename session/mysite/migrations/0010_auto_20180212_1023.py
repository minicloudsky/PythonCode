# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-12 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Letter',
        ),
        migrations.DeleteModel(
            name='Passage',
        ),
        migrations.RemoveField(
            model_name='post',
            name='mood',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Mood',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]