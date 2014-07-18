from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state_province = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    wikipedia = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    wikipedia = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['last_name']

class Book(models.Model):
    title = models.CharField(max_length=100, blank=True)
    authors = models.ManyToManyField(Author, blank=True)
    publisher = models.ForeignKey(Publisher)
    #disalow null
    serial_year = models.IntegerField(blank=True, null=True)
    publication_year = models.IntegerField(blank=True, null=True)
    printed_edition = models.IntegerField(blank=True, null=True)
    wikipedia = models.CharField(max_length=255, blank=True)
 
    def __unicode__(self):
        return self.title

    #class Meta:
    #    ordering = ['publication_year']
