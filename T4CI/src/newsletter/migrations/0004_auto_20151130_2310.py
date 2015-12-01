# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_teammember'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, null=True, blank=True)),
                ('status', models.CharField(max_length=120, null=True, blank=True)),
                ('dreamid', models.PositiveIntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='name',
        ),
    ]
