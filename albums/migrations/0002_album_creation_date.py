# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 06:00
from __future__ import unicode_literals

from django.utils import timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='creation_date',
            field=models.DateTimeField(default=timezone.now, verbose_name='creation date'),
        ),
    ]
