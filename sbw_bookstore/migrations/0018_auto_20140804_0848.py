# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbw_bookstore', '0017_auto_20140804_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='back_cover',
            field=models.ImageField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='colophon',
            field=models.ImageField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='end_pages_back',
            field=models.ImageField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='end_pages_front',
            field=models.ImageField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='half_title',
            field=models.ImageField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='spine',
            field=models.ImageField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.ImageField(null=True, upload_to=b'photos/%Y_%m_%d', blank=True),
        ),
    ]
