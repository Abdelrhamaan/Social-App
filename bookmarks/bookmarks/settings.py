"""
Django settings for bookmarks project.

Generated by 'django-admin startproject' using Django 4.1.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v!stza$_rd5$59dgy#^^q$*&xwdlu%u=+&zqz@w%=iik($k)$-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ABSOLUTE_URL_OVERRIDES = {
    'auth.user':lambda u : reverse_lazy('user_detail',
                                        args=[u.username])
}


# LOGIN_REDIRECT_URL: Tells Django which URL to redirect the user to after a successful login
# if no next parameter is present in the request
# LOGIN_URL: The URL to redirect the user to log in (for example, views using the login_required
# LOGOUT_URL: The URL to redirect the user to log out
# decorator)
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


# Application definition

INSTALLED_APPS = [
    'images.apps.ImagesConfig',
    'account.apps.AccountConfig',
    'actions.apps.ActionsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'django_extensions',
    'easy_thumbnails',
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',#--> must be before any middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookmarks.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'bookmarks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Sending Email ( email server connection )
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'abdelrhmanmamdouh776@gmail.com'
EMAIL_HOST_PASSWORD = 'ryxgxijzvdhfafgd'
EMAIL_PORT = '587'
# to use transport layer security
EMAIL_USE_TLS = True

SITE_ID = 1


# for media (images) url
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


# for building a custom authentication backend
# now you can login with email or password
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
]


# this line to allow hosts
ALLOWED_HOSTS=['mysite.com', 'localhost', '127.0.0.1']

SOCIAL_AUTH_FACEBOOK_KEY = '668767538652175' # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'e4a56e9764ca1dfebf8227e784c16cc9' # Facebook App Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '918635543000-iq1p21t324v0cr33n4ocsq3ajel8g2ol.apps.googleusercontent.com' # Google Client ID
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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' # Google Client Secret

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']



# pipe line to automatic create profile with user who sign 
# with google or facebook account 
SOCIAL_AUTH_PIPELINE = [
'social_core.pipeline.social_auth.social_details',
'social_core.pipeline.social_auth.social_uid',
'social_core.pipeline.social_auth.auth_allowed',
'social_core.pipeline.social_auth.social_user',
'social_core.pipeline.user.get_username',
'social_core.pipeline.user.create_user',
'account.authentication.create_profile',
'social_core.pipeline.social_auth.associate_user',
'social_core.pipeline.social_auth.load_extra_data',
'social_core.pipeline.user.user_details',
]

if DEBUG:
    import mimetypes
    mimetypes.add_type('application/javascript', '.js', True)
    mimetypes.add_type('text/css', '.css', True)


INTERNAL_IPS = [
    '127.0.0.1',
]


REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0