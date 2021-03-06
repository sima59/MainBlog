"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.0.11.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.conf import settings
from django.urls import reverse_lazy
from pathlib import Path

import braintree
#from dotenv import load_dotenv
#load_dotenv()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@fbb-km*%9%58%7jva+=9j3a(s&ecxlgfyo4#nsn*2bu5gng&)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

#CRISPY_TEMPLATE_PACK = 'bootstrap3'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'taggit',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.postgres',
    'shop.apps.ShopConfig',
    'crispy_forms',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    #'payment.apps.PaymentConfig',
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


ROOT_URLCONF = 'myshop.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
   'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'NAME': 'blog',
      'USER': 'blog',
      'PASSWORD': 'sima12345',
    }
}



#WSGI_APPLICATION = 'mysite.wsgi.application'
#WSGI_APPLICATION = 'blog_deploy.wsgi.application'
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
# MEDIA/UPLOADS
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CART_SESSION_ID = 'cart'

# E-mail
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')

# Django crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# cart


#braintree
#BRAINTREE_MERCHANT_ID = os.getenv('BRAINTREE_MERCHANT_ID');     # Merchant ID
#BRAINTREE_PUBLIC_KEY = os.getenv('BRAINTREE_PUBLIC_KEY')        # Public Key
#BRAINTREE_PRIVATE_KEY = os.getenv('BRAINTREE_PRIVATE_KEY')      # Private key
#BRAINTREE_CONF = braintree.Configuration(
#    braintree.Environment.Sandbox,
#    BRAINTREE_MERCHANT_ID,
#    BRAINTREE_PUBLIC_KEY,
#    BRAINTREE_PRIVATE_KEY
#)

#ADMINS = (
 #   (
  #      os.environ.get('ADMIN_NAME'),
   #     os.environ.get('ADMIN_EMAIL')
    #),
#)

# Braintree settings

# Braintree settings
BRAINTREE_MERCHANT_ID = ''  # Merchant ID
BRAINTREE_PUBLIC_KEY = ''   # Public Key
BRAINTREE_PRIVATE_KEY = ''  # Private key

#import braintree

BRAINTREE_MERCHANT_ID = os.getenv('BRAINTREE_MERCHANT_ID');     # Merchant ID
BRAINTREE_PUBLIC_KEY = os.getenv('BRAINTREE_PUBLIC_KEY')        # Public Key
BRAINTREE_PRIVATE_KEY = os.getenv('BRAINTREE_PRIVATE_KEY')      # Private key
BRAINTREE_CONF = braintree.Configuration(
    braintree.Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)

ADMINS = (
    (
        os.environ.get('ADMIN_NAME'),
        os.environ.get('ADMIN_EMAIL')
    ),
)