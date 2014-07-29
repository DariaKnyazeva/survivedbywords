# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbw_bookstore', '0004_author_full_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': [b'full_name']},
        ),
        migrations.RemoveField(
            model_name='author',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
    ]
