# Generated by Django 2.2.4 on 2019-12-01 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passage', '0002_passage_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passage',
            name='background_img',
            field=models.CharField(blank=True, max_length=2000, verbose_name='文章背景图片'),
        ),
    ]
