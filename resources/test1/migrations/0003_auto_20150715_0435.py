# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_auto_20150714_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test1',
            old_name='test2s',
            new_name='test2',
        ),
    ]
