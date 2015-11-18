# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_dream'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, null=True, blank=True)),
                ('personid', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('dreamid', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('position', models.CharField(default=b'TM', max_length=2, choices=[(b'TL', b'Team Leader'), (b'TM', b'Team Member')])),
            ],
        ),
    ]
