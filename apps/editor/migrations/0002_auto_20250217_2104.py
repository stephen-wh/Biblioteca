# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2025-02-17 21:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='editor',
            old_name='estadio',
            new_name='estado',
        ),
    ]
