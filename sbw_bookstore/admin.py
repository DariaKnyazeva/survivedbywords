from django.contrib import admin
from sbw_bookstore.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'wikipedia')
    search_fields = ('full_name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_authors', 'printed_year')
    search_fields = ('title', 'subtitle', 'printed_year')

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)


