from pathlib import Path
from typing import Final

from . import env_config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env_config.ENV__SECRET_KEY
DEBUG = env_config.ENV__DEBUG
ALLOWED_HOSTS = [env_config.ENV__ALLOWED_HOSTS]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "drf_yasg",

    "apps.users.apps.UsersConfig",
    "apps.tasks.apps.TasksConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "settings.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "settings.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env_config.ENV__DATABASE_NAME,
        "USER": env_config.ENV__DATABASE_USER,
        "PASSWORD": env_config.ENV__DATABASE_PASSWORD,
        "HOST": env_config.ENV__DATABASE_HOST,
        "PORT": env_config.ENV__DATABASE_PORT
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Adak"

USE_I18N = True
USE_TZ = True

AUTH_USER_MODEL = 'users.Users'

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


class SuffixRouter:
    SUFFIX_API: Final[str] = "api/v1/"

    TASKS: Final[str] = f"{SUFFIX_API}tasks"
    CATEGORIES: Final[str] = f"{SUFFIX_API}categories"