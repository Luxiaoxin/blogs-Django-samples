# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 03:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20171221_1138'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book1',
            new_name='Books',
        ),
    ]