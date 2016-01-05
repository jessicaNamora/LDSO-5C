# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('messageType', models.PositiveIntegerField(default=4, choices=[(0, b'Invitation'), (1, b'Declined'), (2, b'Accepted'), (3, b'Role Change')])),
                ('receiver', models.PositiveIntegerField(null=True, blank=True)),
                ('dreamid', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('extra', models.CharField(max_length=150, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='responsibleid',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(null=True, upload_to=b'profile_pic', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='locality',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
