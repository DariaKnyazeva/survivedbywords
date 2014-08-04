# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbw_bookstore', '0018_auto_20140804_0848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='colophon',
            new_name='colophon_page',
        ),
        migrations.AddField(
            model_name='book',
            name='title_page',
            field=models.ImageField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
