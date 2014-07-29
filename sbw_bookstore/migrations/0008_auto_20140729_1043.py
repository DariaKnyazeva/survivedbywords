# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbw_bookstore', '0007_book_isbn'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': [b'title']},
        ),
        migrations.AlterField(
            model_name='book',
            name='wikipedia',
            field=models.URLField(max_length=255, blank=True),
        ),
    ]
