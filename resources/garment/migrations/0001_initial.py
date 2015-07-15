# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Garment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product', models.CharField(max_length=256)),
                ('status', models.CharField(max_length=256)),
                ('color', models.CharField(max_length=256)),
                ('season', models.CharField(max_length=256)),
                ('brand', models.CharField(max_length=256)),
                ('size', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('gender', models.CharField(max_length=256)),
                ('type', models.CharField(max_length=256)),
                ('version', models.CharField(max_length=256)),
                ('hasMesh', models.BooleanField(default=False)),
                ('hasTexture', models.BooleanField(default=False)),
                ('pattern', models.ForeignKey(related_name='garment', to='pattern.Pattern')),
            ],
        ),
    ]
