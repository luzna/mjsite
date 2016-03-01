# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_concert_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='content',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
