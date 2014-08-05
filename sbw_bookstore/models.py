from django.db import models
import uuid
import os
import time

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('photos/' + time.strftime("%Y_%m_%d"), filename)

class Publisher(models.Model):
    name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state_province = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    wikipedia = models.URLField(max_length=255, blank=True)
    notes = models.TextField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Author(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    wikipedia = models.URLField(max_length=255, blank=True)
    notes = models.TextField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.full_name)

    class Meta:
        ordering = ['full_name']

class Book(models.Model):
    title = models.CharField(max_length=255, blank=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    authors = models.ManyToManyField(Author, blank=True)
    publisher = models.ForeignKey(Publisher)
    serial_year = models.IntegerField(blank=True, null=True)
    first_published = models.IntegerField(blank=True, null=True)
    printed_year = models.IntegerField(blank=True, null=True)
    printed_edition = models.IntegerField(blank=True, null=True)
    wikipedia = models.URLField(max_length=255, blank=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    dewy = models.CharField(max_length=30, blank=True, null=True)
    notes = models.TextField(max_length=255, blank=True, null=True)
    signed = models.NullBooleanField(blank=True, null=True, default="Unknown")
    front_cover = models.FileField(blank=True, null=True, upload_to=get_file_path)
    back_cover = models.FileField(blank=True, null=True, upload_to=get_file_path)
    spine = models.FileField(blank=True, null=True, upload_to=get_file_path)
    end_pages_front = models.FileField(blank=True, null=True, upload_to=get_file_path)
    inscription = models.FileField(blank=True, null=True, upload_to=get_file_path)
    end_pages_back = models.FileField(blank=True, null=True, upload_to=get_file_path)
    half_title = models.FileField(blank=True, null=True, upload_to=get_file_path)
    title_page = models.FileField(blank=True, null=True, upload_to=get_file_path)
    colophon_page = models.FileField(blank=True, null=True, upload_to=get_file_path)
    top_view = models.FileField(blank=True, null=True, upload_to=get_file_path)
    bottom_view = models.FileField(blank=True, null=True, upload_to=get_file_path)
 
    def __unicode__(self):
        return self.title

    def get_authors(self):
        return "\n".join([a.full_name for a in self.authors.all()])

    def get_title(self):
        if self.subtitle:
            self.subtitle = " - %s" % self.subtitle  
        return ("%s %s" % (self.title, self.subtitle))

    get_authors.short_description = 'Authors'

    class Meta:
        ordering = ['title']

