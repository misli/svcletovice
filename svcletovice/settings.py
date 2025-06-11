from django.utils.translation import ugettext_lazy as _
from leprikon.site.settings import *


SERVER_EMAIL = '"Můj Letokruh" <svcletovice@leprikon.cz>'


# Application definition
INSTALLED_APPS = [
    'svcletovice',
] + INSTALLED_APPS + [
    'cms_articles',
    'cmsplugin_iframe2',
    'django.contrib.redirects',
    'django_mailbox',
    'aldryn_bootstrap3',
    'aldryn_search',
    'cmsplugin_survey',
    'djangocms_column',
    'djangocms_video',
]

MIDDLEWARE = [
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
] + MIDDLEWARE

ROOT_URLCONF = 'svcletovice.urls'

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

# overridden translations
_('instruction on OSH')
_('Registering is currently not allowed.')
_('The capacity of this %(subject_type)s has already been filled. You may register anyway, but the registration may not be approved. We will inform You.')

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
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

CMSPLUGIN_FILER_FOLDER_STYLE_CHOICES = [
    ('gallery', _('Gallery')),
    ('homepage', _('Homepage'))
]

CMSPLUGIN_SURVEY_TEMPLATES = [
    ('default', _('default')),
    ('without_summary', _('without summary')),
]
