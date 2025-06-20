import os
from datetime import timedelta
from pathlib import Path
try:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    sentry_sdk = None
    DjangoIntegration = None

from django.conf import settings

# ─────────────────────────────────────────────────────
# BASE CONFIG
# ─────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-default-key')  # Override via env

DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = (
    os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1,.lvh.me').split(',')
    if not DEBUG else ['*']
)

LOG_DIR = BASE_DIR / 'erp_main' / 'logs'

LOG_DIR.mkdir(parents=True, exist_ok=True)  # ✅ ensures log folder exists

# ─────────────────────────────────────────────────────
# APPLICATIONS
# ─────────────────────────────────────────────────────

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
]

LOCAL_APPS = [
    'erp_main',
    'user_auth.apps.UserAuthConfig',
    'crm.apps.CrmConfig',
    'finance.apps.FinanceConfig',
    'hrms.apps.HrmsConfig',
    'inventory.apps.InventoryConfig',
    'itam.apps.ItamConfig',
    'itsm.apps.ItsmConfig',
    'itom.apps.ItomConfig',
    'vms.apps.VmsConfig',
    'gst.apps.GstConfig',
]


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# ─────────────────────────────────────────────────────
# CUSTOM USER MODEL
# ─────────────────────────────────────────────────────

AUTH_USER_MODEL = 'user_auth.User'


# ─────────────────────────────────────────────────────
# MIDDLEWARE
# ─────────────────────────────────────────────────────

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'erp_main.middleware.TenantMiddleware',  # Custom multi-tenant support
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ─────────────────────────────────────────────────────
# CORS
# ─────────────────────────────────────────────────────
# CORS_ALLOWED_ORIGINS = [
#     "https://app.myfrontend.com",
#     "https://admin.myfrontend.com",
# ]
#
# CORS_ALLOW_CREDENTIALS = False

CORS_ALLOW_ALL_ORIGINS = True

# ─────────────────────────────────────────────────────
# LOGGING
# ─────────────────────────────────────────────────────

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '[{levelname}] {asctime} {name} [{module}:{lineno}] - {message}',
            'style': '{',
        },
        'simple': {
            'format': '[{levelname}] {message}',
            'style': '{',
        },
    },

    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': str(LOG_DIR / 'app.log'),
            'formatter': 'verbose',
        },
        'console': {  # optional: also logs to terminal
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        # Optional: Add Sentry handler if you're using Sentry SDK
        # 'sentry': {
        #     'level': 'ERROR',
        #     'class': 'sentry_sdk.integrations.logging.EventHandler',
        # },
    },

    'root': {
        'handlers': ['file', 'console'],  # add 'sentry' if needed
        'level': 'INFO',
    },

    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}


# ─────────────────────────────────────────────────────
# Sentry
# ─────────────────────────────────────────────────────
# sentry_sdk.init(
#     dsn="https://<your_key>@o123456.ingest.sentry.io/123456",
#     integrations=[DjangoIntegration()],
#     traces_sample_rate=1.0,
#     send_default_pii=True
# )

# ─────────────────────────────────────────────────────
# URLS / WSGI
# ─────────────────────────────────────────────────────

ROOT_URLCONF = 'erp_main.urls'
WSGI_APPLICATION = 'erp_main.wsgi.application'


# ─────────────────────────────────────────────────────
# DATABASES
# ─────────────────────────────────────────────────────

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'mydb'),
        'USER': os.getenv('POSTGRES_USER', 'tess'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'pass'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', '5433'),
    }
}

DATABASE_ROUTERS = ['erp_main.db_router.TenantRouter']

# ─────────────────────────────────────────────────────
# REST FRAMEWORK
# ─────────────────────────────────────────────────────

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'user_auth.auth.TenantJWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

SIMPLE_JWT = {
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': settings.SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# ─────────────────────────────────────────────────────
# PASSWORD VALIDATION
# ─────────────────────────────────────────────────────

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ─────────────────────────────────────────────────────
# REDIS
# ─────────────────────────────────────────────────────
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'KEY_PREFIX': 'erp',
    }
}


# ─────────────────────────────────────────────────────
# TEMPLATES
# ─────────────────────────────────────────────────────

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ─────────────────────────────────────────────────────
# STATIC / MEDIA FILES
# ─────────────────────────────────────────────────────

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ─────────────────────────────────────────────────────
# I18N / TIMEZONE
# ─────────────────────────────────────────────────────

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True


# ─────────────────────────────────────────────────────
# ZABBIX CONFIGURATION
# ─────────────────────────────────────────────────────

ZABBIX_URL = os.getenv('ZABBIX_URL', 'http://localhost:8081')
ZABBIX_USER = os.getenv('ZABBIX_USER', '')
ZABBIX_PASSWORD = os.getenv('ZABBIX_PASSWORD', '')


# ─────────────────────────────────────────────────────
# DEFAULT PRIMARY KEY FIELD
# ─────────────────────────────────────────────────────

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
