# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-03 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20160603_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioitem',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=50),
        ),
    ]
