# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sbw_bookstore.models


class Migration(migrations.Migration):

    dependencies = [
        ('sbw_bookstore', '0027_auto_20140805_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='back_cover',
            field=models.FileField(null=True, upload_to=sbw_bookstore.models.get_file_path, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='bottom_view',
            field=models.FileField(null=True, upload_to=sbw_bookstore.models.get_file_path, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='colophon_page',
            field=models.FileField(null=True, upload_to=sbw_bookstore.models.get_file_path, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='end_pages_back',
            field=models.FileField(null=True, upload_to=sbw_bookstore.models.get_file_path, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='end_pages_front',
            field=models.FileField(null=True, upload_to=sbw_bookstore.models.get_file_path, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='front_cover',
            field=models.FileField(null=True, upload_to=sbw_bookstore.models.get_file_path, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='half_title',
            field=models.FileField(null=True, upload_to=sbw_bookstore.models.get_file_path, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='inscription',
            field=models.FileField(null=True, upload_to=sbw_bookstore.models.get_file_path, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='spine',
            field=models.FileField(null=True, upload_to=sbw_bookstore.models.get_file_path, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title_page',
            field=models.FileField(null=True, upload_to=sbw_bookstore.models.get_file_path, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='top_view',
            field=models.FileField(null=True, upload_to=sbw_bookstore.models.get_file_path, blank=True),
        ),
    ]
