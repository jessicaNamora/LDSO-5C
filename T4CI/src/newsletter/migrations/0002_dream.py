# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, null=True, blank=True)),
                ('category', models.CharField(max_length=120, null=True, blank=True)),
                ('theme', models.CharField(max_length=120, null=True, blank=True)),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
            ],
        ),
    ]
