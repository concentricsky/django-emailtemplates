# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-05 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailtemplates', '0004_auto_20161121_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtemplate',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
