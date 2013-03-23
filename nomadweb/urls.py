from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from website.views import NomadPageView

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', NomadPageView.as_view(), name='home'),
    url(r'^contact/$', 'website.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

