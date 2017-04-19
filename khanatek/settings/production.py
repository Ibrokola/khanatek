from __future__ import absolute_import, unicode_literals

import os

from .base import *


DEBUG = False
# TEMPLATES[0]['OPTIONS']['debug'] = False

SECRET_KEY='riv_tsm@)$i+&$plnqm1i5h4m4yhr2#z%#465o4i&_*d-9nlws' 

# Allow all host headers
ALLOWED_HOSTS = ['khanatek.herokuapp']

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

# DATABASES = {
#     'default':config('DATABASE_URL', default=default_dburl, cast=dburl),
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

import dj_database_url
db_from_env = dj_database_url.config()
DATABASE['default'].update(db_from_env)


# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

try:
    from .local import *
except ImportError:
    pass