from __future__ import absolute_import, unicode_literals

from .base import *


# SECURITY WARNING: don't run with debug turned on in production!

# TEMPLATES[0]['OPTIONS']['debug'] = True


# SECURITY WARNING: keep the secret key used in production secret!


INTERNAL_IPS = ('127.0.0.1')

BASE_URL = 'http://localhost:8000'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
