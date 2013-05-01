from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from website.views import NomadPageView, SubscriberCreateView
from website.feeds import LatestEntries, LatestEntriesDjango, LatestEntriesPython

admin.autodiscover()

MULTIBLOG = getattr(settings, 'NOMADBLOG_MULTIPLE_BLOGS', False)

urlpatterns = patterns('',
    url(r'^$', NomadPageView.as_view(), name='home'),
    url(r'^jobs/$', TemplateView.as_view(template_name="jobs.html"), name='jobs'),
    url(r'^jobs/python/$', TemplateView.as_view(template_name="python_jobs.html"), name='python_jobs'),
    url(r'^contact/$', 'website.views.contact', name='contact'),
    url(r'^subscribe/$', SubscriberCreateView.as_view(), name='subscribe'),
    url(r'^blog/', include('nomadblog.urls')) if not MULTIBLOG else (r'^blogs/(?P<blog_slug>[-\w]+)/', include('nomadblog.urls')),
    url(r'^feeds/latest/$', LatestEntries()),
    url(r'^feeds/django/$', LatestEntriesDjango()),
    url(r'^feeds/python/$', LatestEntriesPython()),
    url(r'^%s' % settings.ADMIN_URL, include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

