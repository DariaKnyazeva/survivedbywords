# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbw_bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='first_published',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
