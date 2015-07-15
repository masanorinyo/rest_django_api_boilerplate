# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test1',
            old_name='test2',
            new_name='test2s',
        ),
    ]
