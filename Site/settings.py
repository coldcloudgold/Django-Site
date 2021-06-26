import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "supersecretkey")


DEBUG = True if os.environ.get("DJANGO_DEBUG") else False


ALLOWED_HOSTS = [
    os.environ.get("DJANGO_ALLOWED_HOSTS", "*"),
    "localhost",
    "127.0.0.1",
]


INSTALLED_APPS = [
    "Posts.apps.PostsConfig",  # APPS
    "Users.apps.UsersConfig",  # APPS
    "Feed_RSS.apps.FeedRssConfig",  # APPS
    "django.contrib.sites",  # Multi-site
    "django.contrib.flatpages",  # Flatpages
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "sorl.thumbnail",  # Image
    "psycopg2",  # DB
    "ckeditor",  # WYSIWYG
    "ckeditor_uploader",  # WYSIWYG
    "allauth",  # User
    "allauth.account",  # User
    "allauth.socialaccount",  # User
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


ROOT_URLCONF = "Site.urls"


TEMPLATES_DIR = BASE_DIR.joinpath("templates")
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]


WSGI_APPLICATION = "Site.wsgi.application"


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


LANGUAGE_CODE = "ru"
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR.joinpath("static")

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR.joinpath("media")


CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    "default": {
        'width': "100%",
        "toolbar_YourCustomToolbarConfig": [
            {
                "name": "basicstyles",
                "items": [
                    "Bold",
                    "Italic",
                    "Underline",
                    "Strike",
                    "Subscript",
                    "Superscript",
                    "-",
                    "RemoveFormat",
                ],
            },
            {
                "name": "paragraph",
                "items": [
                    "NumberedList",
                    "BulletedList",
                    "-",
                    "Blockquote",
                    "-",
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                ],
            },
            {
                "name": "links",
                "items": [
                    "Link",
                    "Unlink",
                ],
            },
            {
                "name": "insert", "items": ["HorizontalRule"]
                },
            "/",
            {
                "name": "styles", "items": ["Format"]
                },
            "/",
            {
                "name": "yourcustomtools",
                "items": [
                    "Preview",
                    "Maximize",
                ],
            },
        ],
        "toolbar": "YourCustomToolbarConfig",
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        "tabSpaces": 4,
        "extraPlugins": ",".join(
            [
                # your extra plugins here
                "div",
                "autolink",
                "autoembed",
                "embedsemantic",
                "autogrow",
                # 'devtools',
                "widget",
                "lineutils",
                "clipboard",
                "dialog",
                "dialogui",
                "elementspath",
            ]
        ),
    }
}


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ID site (flatpage)
SITE_ID = 1


# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "LVL: {levelname}; TM: {asctime}; MDL: {module}; MSG: {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": BASE_DIR.joinpath(
                os.environ.get("LOGGING_NAME", "logging.log")
            ),
            "formatter": "verbose",
        },
    },
    "loggers": {
        "Posts": {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": True,
        },
    },
}

# Login
# LOGIN_URL =
LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "index"


ADMINS = (("Admin", os.environ.get("DJANGO_EMAIL_HOST_USER")),)


if DEBUG:
    # Mail
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = BASE_DIR.joinpath("dev_send_mail")

    # Memcahe
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "dev_memcache",
        }
    }

    # DB
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "dev_database.db",
        }
    }

    # APPS
    INSTALLED_APPS += [
        "allauth.socialaccount.providers.vk",  # VK
        "allauth.socialaccount.providers.github",  # GH
        "django_extensions",  # Shell_plus
    ]

    #  Social
    SOCIALACCOUNT_PROVIDERS = {
        "vk": {
            "APP": {
                "client_id": os.environ.get("SOCIALACCOUNT_PROVIDERS_CLIENT_ID_VK"),
                "secret": os.environ.get("SOCIALACCOUNT_PROVIDERS_SECRET_VK"),
                "key": os.environ.get("SOCIALACCOUNT_PROVIDERS_KEY_VK"),
            }
        },
        "github": {
            "APP": {
                "client_id": os.environ.get("SOCIALACCOUNT_PROVIDERS_CLIENT_ID_GH"),
                "secret": os.environ.get("SOCIALACCOUNT_PROVIDERS_SECRET_GH"),
            },
        },
    }

    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_VERIFICATION = "mandatory"
    ACCOUNT_CONFIRM_EMAIL_ON_GET = True
    ACCOUNT_AUTHENTICATION_METHOD = "username"
    ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "/accounts/login/"
    ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "index"
    ACCOUNT_LOGOUT_REDIRECT_URL = LOGOUT_REDIRECT_URL

else:
    # Mail
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = os.environ.get("DJANGO_EMAIL_HOST")
    EMAIL_HOST_USER = os.environ.get("DJANGO_EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.environ.get("DJANGO_EMAIL_HOST_PASSWORD")
    EMAIL_PORT = os.environ.get("DJANGO_EMAIL_PORT", 587)
    EMAIL_USE_TLS = os.environ.get("DJANGO_EMAIL_USE_TLS", True)

    # Mecache
    MEMCACHED_HOST = os.environ.get("DJANGO_MEMCACHED_HOST")
    MEMCACHED_PORT = os.environ.get("DJANGO_MEMCACHED_PORT", 11211)
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
            "LOCATION": f"{MEMCACHED_HOST}:{MEMCACHED_PORT}",
        }
    }

    # DB
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("DJANGO_DB_ENGINE"),
            "NAME": os.environ.get("DJANGO_DB_DATABASE"),
            "USER": os.environ.get("DJANGO_DB_USER"),
            "PASSWORD": os.environ.get("DJANGO_DB_PASSWORD"),
            "HOST": os.environ.get("DJANGO_DB_HOST"),
            "PORT": os.environ.get("DJANGO_DB_PORT", 5432),
        }
    }

    # Queue
    CELERY_USER = os.environ.get("RABBITMQ_USER")
    CELERY_PASSWORD = os.environ.get("RABBITMQ_PASS")
    CELERY_HOST = os.environ.get("RABBITMQ_HOST")
    CELERY_PORT = os.environ.get("RABBITMQ_PORT", 5672)
    CELERY_BROKER_URL = (
        f"amqp://{CELERY_USER}:{CELERY_PASSWORD}@{CELERY_HOST}:{CELERY_PORT}//"
    )
    CELERY_ACCEPT_CONTENT = ["json"]
    CELERY_TASK_SERIALAIZER = "json"
