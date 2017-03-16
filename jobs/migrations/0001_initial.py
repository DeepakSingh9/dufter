# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=128)),
                ('organisation', models.CharField(max_length=128)),
                ('keyskills', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('experience', models.CharField(max_length=128)),
                ('summary', models.TextField(max_length=500)),
                ('dateposted', models.DateField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='jobcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.JobCategory'),
        ),
    ]