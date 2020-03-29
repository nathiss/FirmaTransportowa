import os
# it's a production-only requirement
# pylint: disable=import-error
import dj_database_url

# pylint: disable=unused-wildcard-import,wildcard-import
from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'False').lower() == 'True'.lower()

ALLOWED_HOSTS = ['firma-transportowa.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

ENVIROMENT = 'production'

DATABASES = {
    'default': dj_database_url.config(default = os.environ['DATABASE_URL'])
}

# Deploy

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'

SECURE_SSL_REDIRECT = True
