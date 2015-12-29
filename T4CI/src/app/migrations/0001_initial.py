# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
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
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=120, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('taskname', models.CharField(max_length=120, null=True, blank=True)),
                ('taskstatus', models.CharField(max_length=120, null=True, blank=True)),
                ('dreamid', models.PositiveIntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('personid', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('dreamid', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('position', models.CharField(default=b'TM', max_length=2, choices=[(b'TL', b'Team Leader'), (b'TM', b'Team Member')])),
            ],
        ),
    ]
