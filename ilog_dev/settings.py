"""
Django settings for ilog_dev project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
# lets understand git
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '887)db5-i5&w5xokel^shduo(cb!3cd&pjh!v+y+!*r^!*o69c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'enterprise',
    'accounts',
    'nodes',
    'message',
    'myuserprofile',
    'enterprise_profile',
    'activities',
    'search',
    'imagekit',
    # 'whoosh',
    # 'haystack'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ilog_dev.urls'

WSGI_APPLICATION = 'ilog_dev.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'ilog_prefinal',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'autocommit': True,
    }
}

# HAYSTACK_CONNECTIONS = {'default': {
#     'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#     'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
#     },
#                         }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'accounts.MyUser'

ROOT_DIR = os.path.abspath("")

MEDIA_ROOT = os.path.join(BASE_DIR, 'images/')
MEDIA_URL = '/images/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    )

STATIC_ROOT = os.path.join(ROOT_DIR, 'templates')

# STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(ROOT_DIR, 'templates/static')]

