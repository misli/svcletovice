# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
Django settings for svcletovice project.
"""

from django.utils.translation import ugettext_lazy as _
from leprikon.site.settings import *

ADMINS = [
    ('Jakub Dorňák', 'jakub.dornak@svcletovice.cz'),
]
MANAGERS = [
    ('Jakub Dorňák', 'jakub.dornak@svcletovice.cz'),
    ('Ivana Dlapová', 'ivana.dlapova@svcletovice.cz'),
]
SERVER_EMAIL = '"Můj Letokruh" <muj-letokruh@svcletovice.cz>'


# Application definition
INSTALLED_APPS = [
    'svcletovice',
    'cms_articles',
    'cmsplugin_iframe2',
] + INSTALLED_APPS + [
    'django.contrib.redirects',
    'django_mailbox',
    'haystack',
    'aldryn_search',
    'cmsplugin_survey',
]

TEMPLATES[0]['OPTIONS']['context_processors'].append('cms_articles.context_processors.cms_articles')

MIDDLEWARE_CLASSES = [
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
] + MIDDLEWARE_CLASSES

ROOT_URLCONF = 'svcletovice.urls'

WSGI_APPLICATION = 'svcletovice.wsgi.application'

CMS_TEMPLATES = [
    ('default.html', _('Default')),
    ('with_submenu.html', _('With submenu')),
    ('home.html', _('Home page')),
]

# templates used to render plugin article
CMS_ARTICLES_PLUGIN_ARTICLE_TEMPLATES = [
    ('default', _('Default')),
    ('home', _('Home page')),
    ('home-3x', _('Home page - 3x')),
]

# templates used to render plugin articles
CMS_ARTICLES_PLUGIN_ARTICLES_TEMPLATES = [
    ('default', _('Default')),
    ('archive', _('Archive')),
    ('home', _('Home page')),
    ('home-3x', _('Home page - 3x')),
]

CMS_PLACEHOLDER_CONF = {
    'content': {
        'name': _('Content'),
    },
    'sidebar': {
        'name': _('Sidebar'),
    },
    'footer-1': {
        'name': _('Footer - column 1'),
    },
    'footer-2': {
        'name': _('Footer - column 2'),
    },
    'footer-3': {
        'name': _('Footer - column 3'),
    },
    'footer-4': {
        'name': _('Footer - column 4'),
    },
}

THUMBNAIL_ALIASES = {
    '': {
        'preview': {
            'size':     (240, 10000)
        },
        'view': {
            'size':     (760, 570)
        },
    },
}

GANALYTICS_TRACKING_CODE = 'UA-88866609-1'

# set to None to allow any value
CMSPLUGIN_IFRAME_CLASSES = [
    (None, _('no class')),
]

# set to None to allow any value
CMSPLUGIN_IFRAME_WIDTHS = [
    ('200', _('200 pixels')),
    ('400', _('400 pixels')),
    ('800', _('800 pixels')),
    ('100%', _('100 %')),
]

# set to None to allow any value
CMSPLUGIN_IFRAME_HEIGHTS = [
    ('150', _('150 pixels')),
    ('300', _('300 pixels')),
    ('600', _('600 pixels')),
    ('1200', _('1200 pixels')),
    ('100%', _('100 %')),
]

# toto funguje až po vytvoření stránky s aplikací Leprikón
LOGIN_URL = 'leprikon:user_login'
LOGOUT_URL = 'leprikon:user_logout'
LOGIN_REDIRECT_URL  = '/muj-letokruh/'

# overridden translations
_('instruction on OSH')

# search settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'data', 'search'),
    },
    'cs': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'data', 'search'),
    },
}

CMSPLUGIN_FILER_FOLDER_STYLE_CHOICES = [
    ('gallery', _('Gallery')),
    ('homepage', _('Homepage'))
]

CMSPLUGIN_SURVEY_TEMPLATES = [
    ('default', _('default')),
    ('without_summary', _('without summary')),
]
