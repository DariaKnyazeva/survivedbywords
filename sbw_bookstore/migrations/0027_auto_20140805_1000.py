# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbw_bookstore', '0026_auto_20140805_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bottom_view',
            field=models.FileField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='inscription',
            field=models.FileField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='top_view',
            field=models.FileField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
            preserve_default=True,
        ),
    ]
