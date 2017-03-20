# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 06:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0004_auto_20170318_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('photo', models.ImageField(blank=True, upload_to='user/%y/%m/%d')),
                ('keyskills', models.CharField(max_length=128)),
                ('experience', models.IntegerField()),
                ('user', models.OneToOneField(max_length=128, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserCreate',
        ),
    ]