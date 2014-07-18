# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, blank=True)),
                ('last_name', models.CharField(max_length=40, blank=True)),
                ('wikipedia', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'ordering': [b'last_name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('serial_year', models.IntegerField(null=True, blank=True)),
                ('publication_year', models.IntegerField(null=True, blank=True)),
                ('printed_edition', models.IntegerField(null=True, blank=True)),
                ('wikipedia', models.CharField(max_length=255, blank=True)),
                ('authors', models.ManyToManyField(to='sbw_bookstore.Author', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
                ('address', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=60, blank=True)),
                ('state_province', models.CharField(max_length=30, blank=True)),
                ('country', models.CharField(max_length=50, blank=True)),
                ('website', models.URLField(blank=True)),
                ('wikipedia', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'ordering': [b'name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(to='sbw_bookstore.Publisher'),
            preserve_default=True,
        ),
    ]
