# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbw_bookstore', '0006_auto_20140729_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=13, null=True, blank=True),
            preserve_default=True,
        ),
    ]
