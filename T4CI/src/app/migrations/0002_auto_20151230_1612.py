# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='active',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='position',
            field=models.CharField(default=b'TM', max_length=2, choices=[(b'TL', b'Team Leader'), (b'TM', b'Team Member'), (b'TC', b'Team Communicator')]),
        ),
    ]
