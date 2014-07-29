# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbw_bookstore', '0008_auto_20140729_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='wikipedia',
            field=models.URLField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='wikipedia',
            field=models.URLField(max_length=255, blank=True),
        ),
    ]
