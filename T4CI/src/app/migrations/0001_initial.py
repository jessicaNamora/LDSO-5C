# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
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
                ('dateCreated', models.DateTimeField(default=datetime.date.today, blank=True)),
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
                ('position', models.CharField(default=b'TM', max_length=2, choices=[(b'TL', b'Team Leader'), (b'TM', b'Team Member'), (b'TC', b'Team Communicator')])),
                ('active', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(max_length=150, null=True)),
                ('locality', models.CharField(max_length=30, null=True)),
                ('phone_number', models.PositiveIntegerField(null=True)),
                ('description', models.CharField(max_length=150, null=True)),
                ('avatar', models.ImageField(default=b'default.png', upload_to=b'profile_pic')),
            ],
        ),
    ]
