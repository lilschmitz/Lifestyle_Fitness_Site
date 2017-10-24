"""
Django settings for KS_Stream_3_LifestyleFitnessCoaching project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os.path
#import env
# => once POSTGRES set up else comment out import  dj_database_url
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret! = > has been configured as part of configurations
SECRET_KEY = os.environ.get('SECRET_KEY')



# SECURITY WARNING: don't run with debug turned on in production! =>  has been configured as part of configurations
DEBUG = os.environ.get('DEBUG', False)


# Heroku hosting configurations !!!
ALLOWED_HOSTS = ['lifestylefitnesscoaching.heroku.com', '127.0.0.1']
INTERNAL_IPS = ['127.0.0.1']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',
    'django.contrib.sites',
    'disqus',
    'django_gravatar',
    'home',
    'stripe',
    'accounts',
    'contacts',
    'profiles',
    'blog',
    'services',
    'payments',
    'cart'

]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',


]

ROOT_URLCONF = 'KS_Stream_3_LifestyleFitnessCoaching.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [

            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.media',
            'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'KS_Stream_3_LifestyleFitnessCoaching.wsgi.application'

# below would be commented out if running app local in Pycharm without Heroku
DATABASES={'default':dj_database_url.parse(os.environ.get('DATABASE_URL')) }

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# COMMENT out the sqlite backends once deploying to HEROKU

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth'
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



#STRIPE

STRIPE_PUBLISHABLE = os.environ.get('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_VERSION = os.environ.get('STRIPE_VERSION')


#TRYING DJstripe see for documentation https://github.com/dj-stripe/dj-stripe

# # STRIPE_LIVE_PUBLIC_KEY = os.environ.get("STRIPE_LIVE_PUBLIC_KEY")
# # STRIPE_LIVE_SECRET_KEY = os.environ.get("STRIPE_LIVE_SECRET_KEY")
# STRIPE_TEST_PUBLIC_KEY = os.environ.get('STRIPE_TEST_PUBLIC_KEY')
# STRIPE_TEST_SECRET_KEY = os.environ.get('STRIPE_TEST_SECRET_KEY')
# STRIPE_LIVE_MODE = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# Simplified static file serving. => https://devcenter.heroku.com/articles/django-assets
# https://warehouse.python.org/project/whitenoise/
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Commented out below for static and media in order to run Heroku deployment using AWS S3

# STATIC_URL = '/static/'
# STATICFILES_DIRS = ( os.path.join('static'), )

#Configuration of the media route for uploads

# Commented out below for static and media in order to run Heroku deployment using AWS S3

# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# MEDIA_URL = '/media/'




SITE_ID = 1

# Email Settings

DEFAULT_FROM_EMAIL = 'kathrinlschmitz@example.com'

# To use Django's Console email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DISQUS_WEBSITE_SHORTNAME = 'lifestyle-fitness'
SITE_ID = 1


AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY= os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_HOST ='s3-eu-west-1.amazonaws.com'


#below creates a custom domain/subdirectory static storage loaction in the storage bucket
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)


#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'Cache-Control': 'max-age=94608000',
    }