# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 05:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_auto_20170813_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('underlying', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='accounts.Account')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='position',
            unique_together=set([('account', 'underlying')]),
        ),
    ]
