"""
Django settings for proyecto project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import sys
import base64
import hashlib
import redis
from channels.layers import get_channel_layer

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%mr0+6-7m&)eo5p-=n83bs3g260hsf60p81@h!qt64j_i00)b7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

BLOG_NAME = 'MarviCare'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'proyecto',
    'inicio',
    'django.contrib.humanize',
    'usuarios',
    'taggit',
    'channels',
    'mensajes',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyecto.urls'

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # Carpeta principal de plantillas
            os.path.join(BASE_DIR, 'inicio', 'templates'),  # Carpeta de plantillas de inicio
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



WSGI_APPLICATION = 'proyecto.wsgi.application'

ASGI_APPLICATION = 'proyecto.asgi.application'

# Configura tus claves de cifrado simétrico
DJANGO_SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'TVSb3HUCuhXvFwo3v4ekUFbcJWesmb5J')

# Configuración de Redis Cloud
REDIS_HOST = 'redis-15137.c304.europe-west1-2.gce.redns.redis-cloud.com'
REDIS_PORT = 15137
REDIS_PASSWORD = 'TVSb3HUCuhXvFwo3v4ekUFbcJWesmb5J'

# Configuración de CHANNEL_LAYERS
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [{
                'address': f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}',
            }],
            'capacity': 100,  # Ajusta según tus necesidades
            'expiry': 60 * 5,  # Ajusta según tus necesidades
            'group_expiry': 60 * 60 * 24,
            'channel_capacity': {
                'http.request': 100,
                'websocket.receive': 100,
            },
            'symmetric_encryption_keys': [
                base64.urlsafe_b64encode(hashlib.sha256(DJANGO_SECRET_KEY.encode()).digest()).decode()
            ],
        },
    },
}


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/index/'
LOGOUT_REDIRECT_URL = 'login'

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'inicio', 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

