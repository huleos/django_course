# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-17 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20160603_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioitem',
            name='categories',
            field=models.ManyToManyField(blank=True, to='portfolio.Category'),
        ),
    ]