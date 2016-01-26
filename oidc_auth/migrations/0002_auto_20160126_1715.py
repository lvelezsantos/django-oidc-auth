# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-26 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oidc_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='openidprovider',
            name='logout',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='openidprovider',
            name='signing_alg',
            field=models.CharField(choices=[(b'RS256', b'RS256'), (b'HS256', b'HS256')], default=b'RS256', max_length=5),
        ),
    ]
