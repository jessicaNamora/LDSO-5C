# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160105_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('giftid', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('user', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('gift', models.CharField(max_length=30, null=True, blank=True)),
            ],
        ),
    ]
