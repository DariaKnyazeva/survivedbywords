# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbw_bookstore', '0012_auto_20140729_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='signed',
            field=models.NullBooleanField(default=b'Unknown'),
            preserve_default=True,
        ),
    ]
