# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbw_bookstore', '0002_book_first_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publication_year',
            new_name='printed_year',
        ),
    ]
