# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160105_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='seen',
            field=models.BooleanField(default=0),
        ),
    ]
