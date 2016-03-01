# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20151229_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='content',
            field=models.TextField(default=None),
            preserve_default=True,
        ),
    ]
