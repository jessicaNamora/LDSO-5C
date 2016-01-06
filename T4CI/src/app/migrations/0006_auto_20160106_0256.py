# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.date.today, blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='dateFinished',
            field=models.DateTimeField(default=datetime.date.today, blank=True),
        ),
    ]
