# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls_wourl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='api_f',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to=b'wof')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='api_g',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to=b'wog')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='api_h',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to=b'woh')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='api_i',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to=b'woi')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='api_j',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to=b'woj')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='api_k',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to=b'wok')),
                ('description', models.TextField()),
            ],
        ),
    ]
