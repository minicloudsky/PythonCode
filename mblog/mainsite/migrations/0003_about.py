# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-11-28 05:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20171126_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('resume', models.TextField()),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-update_date',),
            },
        ),
    ]
