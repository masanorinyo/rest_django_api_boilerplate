# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0003_auto_20150723_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pattern',
            name='status',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='version',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
