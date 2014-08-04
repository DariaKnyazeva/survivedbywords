from django.conf.urls import patterns, include, url
from django.contrib import admin
from sbw_bookstore.views import hello, book, books, authors
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'survivedbywords.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^books/$', books),
    url(r'^books/(.+)/$', book),
    url(r'^authors/(.+)/$', authors),
    url(r'^authors/(.+)/$', authors),
    url(r'^$', hello),


    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
