# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_search'),
    ]

    operations = [
        migrations.DeleteModel(
            name='api_a',
        ),
        migrations.DeleteModel(
            name='api_b',
        ),
        migrations.DeleteModel(
            name='api_c',
        ),
        migrations.DeleteModel(
            name='api_d',
        ),
        migrations.DeleteModel(
            name='api_east',
        ),
        migrations.DeleteModel(
            name='api_model',
        ),
        migrations.DeleteModel(
            name='api_north',
        ),
        migrations.DeleteModel(
            name='api_south',
        ),
        migrations.DeleteModel(
            name='api_west',
        ),
        migrations.DeleteModel(
            name='search',
        ),
    ]
