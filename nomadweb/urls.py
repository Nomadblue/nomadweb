from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from website.views import NomadPageView, SubscriberCreateView
from website.feeds import LatestEntries, LatestEntriesDjango, LatestEntriesPython

admin.autodiscover()

MULTIBLOG = getattr(settings, 'NOMADBLOG_MULTIPLE_BLOGS', False)

urlpatterns = patterns('',
    url(r'^$', NomadPageView.as_view(), name='home'),
    url(r'^contact/$', 'website.views.contact', name='contact'),
    url(r'^subscribe/$', SubscriberCreateView.as_view(), name='subscribe'),
    url(r'^blog/', include('nomadblog.urls')) if not MULTIBLOG else (r'^blogs/(?P<blog_slug>[-\w]+)/', include('nomadblog.urls')),
    url(r'^feeds/latest/$', LatestEntries()),
    url(r'^feeds/django/$', LatestEntriesDjango()),
    url(r'^feeds/python/$', LatestEntriesPython()),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

