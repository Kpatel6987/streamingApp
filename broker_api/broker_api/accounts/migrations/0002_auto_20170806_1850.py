# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-06 22:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set([('user', 'account_name')]),
        ),
    ]
