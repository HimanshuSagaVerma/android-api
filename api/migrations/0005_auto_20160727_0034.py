# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='api_east',
            name='url',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='api_north',
            name='url',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='api_south',
            name='url',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='api_west',
            name='url',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
