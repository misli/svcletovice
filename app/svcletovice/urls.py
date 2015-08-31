from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # url(regex, view, kwargs=None, name=None, prefix='')
    url(r'', include('django.contrib.staticfiles.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^', include('cms.urls')),
)

