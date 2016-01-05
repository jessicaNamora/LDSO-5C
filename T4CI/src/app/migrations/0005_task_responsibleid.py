# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160104_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='responsibleid',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
        ),
    ]
