# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-11-21 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailtemplates', '0002_auto_20161117_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtemplate',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
