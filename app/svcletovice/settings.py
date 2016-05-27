# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

"""
Django settings for svcletovice project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
    with open(os.path.join(BASE_DIR, 'data', 'secret_key')) as f:
        SECRET_KEY = f.read()
except IOError:
    with open(os.path.join(BASE_DIR, 'data', 'secret_key'), 'w') as f:
        from django.utils.crypto import get_random_string
        SECRET_KEY = get_random_string(50,
            'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
        f.write(SECRET_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG   = os.environ.get('DEBUG', False) and True or False
DBDEBUG = os.environ.get('DEBUG', False) == 'DB'

ALLOWED_HOSTS = ['www.svcletovice.cz', '127.0.0.1']

ADMINS = [
    ('Jakub Dorňák', 'jakub.dornak@svcletovice.cz'),
]
MANAGERS = [
    ('Jakub Dorňák', 'jakub.dornak@svcletovice.cz'),
    ('Hana Sobotková', 'hana.sobotkova@svcletovice.cz'),
]
SERVER_EMAIL = '"Můj Letokruh" <muj-letokruh@svcletovice.cz>'


# Application definition

INSTALLED_APPS = [
    'leprikon',
    'cms_articles',
    'cms_articles.import_wordpress',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.redirects',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'djangocms_text_ckeditor',
    'treebeard',
    'cms',
    'menus',
    'mptt',
    'easy_thumbnails',
    'sekizai',
    'filer',
    'cmsplugin_iframe2',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_link',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    'ganalytics',
    'django_mailbox',
]

MIDDLEWARE_CLASSES = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'leprikon.middleware.LeprikonMiddleware',
]

ROOT_URLCONF = 'svcletovice.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
            'debug': os.environ.get('DEBUG', False) == 'TEMPLATE',
        },
    },
]

WSGI_APPLICATION = 'svcletovice.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data', 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'cs'

TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'htdocs', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'htdocs', 'media')

# Additional locations of static files
STATICFILES_DIRS = [
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static'),
]

SITE_ID = 1

LANGUAGES = [
    ('cs', _('Czech')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'conf', 'locale'),
]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'mail_admins'],
            'level': DEBUG and 'DEBUG' or 'INFO',
            'propagate': True,
        },
        'django.db.backends': {
            'level': DBDEBUG and 'DEBUG' or 'INFO',
            'propagate': True,
        },
    },
}


#####################
# CMS Configuration #
#####################

CMS_LANGUAGES = {
    1: [
        {
            'code': 'cs',
            'name': _('Czech'),
        },
    ],
    'default': {
        'public': True,
        'fallbacks': ['cs'],
        'hide_untranslated': True,
        'redirect_on_fallback': True,
    },
}

CMS_TEMPLATES = [
    ('default.html', _('Default')),
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
}

CACHES = {
    'default': {
        'BACKEND':    'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION':   '127.0.0.1:11211',
        'KEY_PREFIX': 'svcletovice',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

MIGRATION_MODULES = {
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_link': 'cmsplugin_filer_link.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
}

THUMBNAIL_DEBUG = os.environ.get('DEBUG', False) == 'THUMBNAIL'

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

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

GANALYTICS_TRACKING_CODE = 'UA-41666766-1'

PRICE_DECIMAL_PLACES = 0

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

TEST_RUNNER = None

# toto funguje až po vytvoření stránky s aplikací Domeček
LOGIN_URL = 'leprikon:user_login'
LOGOUT_URL = 'leprikon:user_logout'
LOGIN_REDIRECT_URL  = 'leprikon:summary'

# overridden translations
_('instruction on OSH')

