# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20151229_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='content',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
