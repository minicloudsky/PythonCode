# Generated by Django 2.2.8 on 2019-12-30 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passage', '0003_auto_20191201_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='passage',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
    ]
