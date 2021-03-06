from django.conf.urls import patterns, include, url
from django.contrib import admin
from sbw_bookstore.views import hello, book, books, authors
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User, Group
from sbw_bookstore.models import Book, Author, Publisher
from rest_framework import viewsets, routers, serializers

admin.autodiscover()

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle')

class BookViewSet(viewsets.ModelViewSet):
    model = Book

class PublisherViewSet(viewsets.ModelViewSet):
    model = Publisher

class AuthorViewSet(viewsets.ModelViewSet):
    model = Author


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'booksapi', BookViewSet)
router.register(r'publishersapi', PublisherViewSet)
router.register(r'authorsapi', AuthorViewSet)


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'survivedbywords.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^books/$', books),
    url(r'^books/(.+)/$', book),
    url(r'^authors/(.+)/$', authors),
    url(r'^authors/(.+)/$', authors),
    url(r'^$', hello),
    
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

