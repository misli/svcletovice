from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from domecek.urls import club_registration

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^domecek/', include('domecek.urls', 'domecek', 'domecek')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
)

