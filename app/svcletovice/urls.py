"""svcletovice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

import cms.urls

from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

from social.apps.django_app import urls as social_urls
import cmsplugin_survey.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^social/', (social_urls, 'social', 'social')),
    url(r'^survey/', (cmsplugin_survey.urls, 'survey', 'survey')),
    url(r'^', (cms.urls, None, None)),
]

if settings.DEBUG:
    urlpatterns.append(url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}))

