# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_gift'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gift',
            name='giftid',
        ),
    ]
