# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20151130_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dreamer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='name',
        ),
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.AddField(
            model_name='task',
            name='taskname',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='taskstatus',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
