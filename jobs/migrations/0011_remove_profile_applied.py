# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 10:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_profile_applied'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='applied',
        ),
    ]