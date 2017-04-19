from __future__ import absolute_import, unicode_literals

from .base import *

import dj_database_url

import os


env = os.environ.copy()


DEBUG = False
# TEMPLATES[0]['OPTIONS']['debug'] = False

SECRET_KEY='riv_tsm@)$i+&$plnqm1i5h4m4yhr2#z%#465o4i&_*d-9nlws'

# Parse database configuration from $DATABASE_URL
# DATABASES['default'] = dj_database_url.config()

	
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') 

# Allow all host headers
ALLOWED_HOSTS = ['']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}




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