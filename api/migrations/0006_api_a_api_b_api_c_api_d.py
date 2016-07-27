# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20160727_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='api_a',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to=b'a')),
                ('url', models.CharField(max_length=2000, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='api_b',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to=b'b')),
                ('url', models.CharField(max_length=2000, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='api_c',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to=b'c')),
                ('url', models.CharField(max_length=2000, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='api_d',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to=b'd')),
                ('url', models.CharField(max_length=2000, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
