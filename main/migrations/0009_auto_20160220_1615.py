# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20151229_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='checked',
            new_name='approved_comment',
        ),
        migrations.AlterField(
            model_name='concert',
            name='content',
            field=models.TextField(default=datetime.datetime(2016, 2, 20, 15, 15, 58, 949907, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
