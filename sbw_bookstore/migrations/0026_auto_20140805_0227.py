# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbw_bookstore', '0025_auto_20140805_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='back_cover',
            field=models.FileField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='colophon_page',
            field=models.FileField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='end_pages_back',
            field=models.FileField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='end_pages_front',
            field=models.FileField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='half_title',
            field=models.FileField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='spine',
            field=models.FileField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title_page',
            field=models.FileField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
        ),
    ]
