from django.contrib import admin
from django import forms
from pyuploadcare.dj import FileField, ImageField, ImageGroupField
from sbw_bookstore.models import Publisher, Author, Book
from django.contrib.admin.widgets import AdminFileWidget

class AdminImageWidget(forms.FileField):
    """
    A ImageField Widget for admin that shows a thumbnail.
    """

    def __init__(self, attrs={}):
        super(AdminImageWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            output.append(('<a target="_blank" href="%s">'
                           '<img src="%s" style="height: 28px;" /></a> '
                           % (value.url, value.url)))
        output.append(super(AdminImageWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
    

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'wikipedia')
    search_fields = ('full_name',)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ()
    
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for _name, field in self.fields.items():
            if type(field) == forms.ImageField:
                field.widget=AdminImageWidget()


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_authors', 'printed_year')
    search_fields = ('title', 'subtitle', 'printed_year')
    form = BookForm

    save_as = True

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)


