from django.contrib import admin
from sbw_bookstore.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'wikipedia')
    search_fields = ('full_name',)

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)


