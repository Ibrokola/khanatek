from __future__ import absolute_import, unicode_literals

from .dev import *
from .base import *

import dj_database_url

import os


DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = False


# Parse database configuration from $DATABASE_URL
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES.['default'].update(db_from_env)
	
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') 

# Allow all host headers
ALLOWED_HOSTS = ['*']

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