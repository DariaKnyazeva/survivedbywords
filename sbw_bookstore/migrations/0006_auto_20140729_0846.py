# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbw_bookstore', '0005_auto_20140729_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='subtitle',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
