# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=256)),
                ('test2', models.ForeignKey(related_name='test1', to='test2.Test2')),
            ],
        ),
    ]
