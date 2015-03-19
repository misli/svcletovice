# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

"""
Django settings for svcletovice project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

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

TEMPLATE_DEBUG = os.environ.get('DEBUG', False) == 'TEMPLATE'

ALLOWED_HOSTS = ['www.svcletovice.cz', '127.0.0.1']

ADMINS = (
    ('Jakub Dorňák', 'admin@misli.cz'),
)
MANAGERS = (
    ('Jakub Dorňák', 'admin@misli.cz'),
    ('SVČ Letovice', 'info@ddmletovice.cz'),
)
SERVER_EMAIL = '"WEB SVČ Letovice" <admin@svcletovice.cz>'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'tagging',
    'djangocms_text_ckeditor',
    'cms',
    'mptt',
    'django_mptt_admin',
    'easy_thumbnails',
    'menus',
    'south',
    'sekizai',
    'sortedm2m',
    'filer',
    'domecek',
    'cmsplugin_articles',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_link',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    'captcha',
    'dbtemplates',
    'ganalytics',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'domecek.middleware.SchoolYearMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data', 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'cs'

TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'htdocs', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'htdocs', 'media')

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)

SITE_ID = 1

LANGUAGES = (
    ('cs', _('Czech')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'conf', 'locale'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings',
    'sekizai.context_processors.sekizai',
)

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

CMS_TEMPLATES = (
    ('default.html', _('Default')),
)

CMS_PLACEHOLDER_CONF = {
    'content': {
        'name': _('Content'),
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

CAPTCHA_FONT_SIZE        = 24
CAPTCHA_LETTER_ROTATION  = None
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
CAPTCHA_FOREGROUND_COLOR = '#001100'
CAPTCHA_CHALLENGE_FUNCT  = 'captcha.helpers.math_challenge'
CAPTCHA_NOISE_FUNCTIONS  = ()
CAPTCHA_FILTER_FUNCTIONS = ()

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

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

# List of callables that know how to import templates from various sources.
# See the comments in django/core/template/loader.py for interface
# documentation.
TEMPLATE_LOADERS = (
    'dbtemplates.loader.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

GANALYTICS_TRACKING_CODE = 'UA-41666766-1'

