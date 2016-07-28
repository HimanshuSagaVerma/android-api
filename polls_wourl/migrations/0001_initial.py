# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='api_a',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to=b'woa')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='api_b',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to=b'wob')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='api_c',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to=b'woc')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='api_d',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to=b'wod')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='api_e',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to=b'woe')),
                ('description', models.TextField()),
            ],
        ),
    ]
