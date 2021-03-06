# Django settings for ibtsocs project.

import os
import sys

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('broder', 'broder@mit.edu'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/__scripts/django/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-u45kzb(dyysp1q4cim)yk==m&ckba&2@&7ot2ki7lbgua$6wa'

FORCE_LOWERCASE_TAGS = True

SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 4

FORCE_SCRIPT_NAME = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'ibtsocs.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'tagging',
    'ibtsocs.root',
)

sys.path[0:0] = os.path.abspath(os.path.dirname(__file__))
try:
    from site import *
except ImportError:
    sys.stderr.write("Please create a 'site.py' file with your local database settings.")
    sys.exit(1)
del sys.path[0]
