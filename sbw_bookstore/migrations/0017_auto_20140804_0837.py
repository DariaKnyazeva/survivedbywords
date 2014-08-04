# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbw_bookstore', '0016_book_front_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='front_cover',
            field=models.ImageField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
        ),
    ]
