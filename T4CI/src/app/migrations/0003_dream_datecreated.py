# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151230_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='dream',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.date.today, blank=True),
        ),
    ]
