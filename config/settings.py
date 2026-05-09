from pathlib import Path
import os
from django.contrib.messages import constants as messages
from decouple import config, Csv

# ── Base ───────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost', cast=Csv())

PROJECT_NAME = config('PROJECT_NAME', default='Nirman Global')

# ── Auth ───────────────────────────────────────────────────────────────────
AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = '/'

# ── Installed Apps ─────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.projects',
    'apps.ai_engine',
    'apps.leads',
    'apps.home',
    'apps.users',
    'apps.services',
    'apps.team',
    'apps.testimonials',
    'apps.contact',
    'apps.site_settings',
    'apps.book_desgin',
    'rest_framework',
]

# ── Middleware ─────────────────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

# ── Templates ──────────────────────────────────────────────────────────────
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

# ── Database ───────────────────────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':     config('DB_NAME',     default='nirmal_db'),
        'USER':     config('DB_USER',     default='nirmal_user'),
        'PASSWORD': config('DB_PASSWORD', default='1234'),
        'HOST':     config('DB_HOST',     default='localhost'),
        'PORT':     config('DB_PORT',     default='5432'),
    }
}

# ── Password Validation ────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ── Internationalisation ───────────────────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'Asia/Kolkata'
USE_I18N      = True
USE_TZ        = True

# ── Static & Media ─────────────────────────────────────────────────────────
STATIC_URL  = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL  = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ── Email ──────────────────────────────────────────────────────────────────
EMAIL_BACKEND      = config('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST         = config('EMAIL_HOST',    default='smtp-relay.brevo.com')
EMAIL_PORT         = config('EMAIL_PORT',    default=587, cast=int)
EMAIL_USE_TLS      = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER    = config('EMAIL_HOST_USER',     default='')
EMAIL_HOST_PASSWORD= config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL',  default='')
ADMIN_EMAIL        = config('ADMIN_EMAIL',         default='')

# Fallback: save emails to disk when SMTP is not configured (dev only)
EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'

# ── Flash message → Bootstrap class mapping ────────────────────────────────
MESSAGE_TAGS = {
    messages.DEBUG:   'alert-secondary',
    messages.INFO:    'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR:   'alert-danger',
}

# ── Third-party API keys ───────────────────────────────────────────────────
OPENAI_API_KEY = config('OPENAI_API_KEY', default='')
GEMINI_API_KEY = config('GEMINI_API_KEY', default='')

# ── Security (production) ──────────────────────────────────────────────────
# These are safe to enable once DEBUG=False and HTTPS is set up
# SECURE_SSL_REDIRECT         = True
# SESSION_COOKIE_SECURE       = True
# CSRF_COOKIE_SECURE          = True
# SECURE_HSTS_SECONDS         = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD         = True
