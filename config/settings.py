import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# apps以下にappを配置するための設定
sys.path.append(os.path.join(BASE_DIR, "apps"))

SECRET_KEY = 't!r7fj7j6+3r)-nk^ddefi(q72ou-o=(4gfqb%6wp=l=yxuva6'
DEBUG = True
ALLOWED_HOSTS = ['*']
API_MODE = True  # APIを呼び出すか，ローカルのJSONファイルを読み込むか

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'apps.account',
    'apps.shift',
    'apps.api',
    'apps.manual',
    'apps.timetable',
    'apps.option',
    'apps.notification',
    'apps.contact',
    'markdownx',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.open_access_middleware',
]

ROOT_URLCONF = 'config.urls'

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

# local_settings.pyにデータベースの情報を書く
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nutfes_shift_app',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'db',
        'PORT': 3306,
        'OPTIONS': {
            'charset': 'utf8',
            'sql_mode': 'TRADITIONAL,NO_AUTO_VALUE_ON_ZERO,ONLY_FULL_GROUP_BY',
        }
    }
}

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

LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MARKDOWN_IMAGE_MAX_SIZE = {'size': (2000, 2000), 'quality': 100}


# CustomUserモデルをAdminに設定
AUTH_USER_MODEL = 'account.User'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

LOGIN_URL = 'account:login'
LOGIN_REDIRECT_URL = 'home'

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
]

# local設定の読み込み
try:
    from .local_settings import *
except ImportError:
    pass

# 各種定数の読み込み
try:
    from .constants import *
except ImportError:
    pass
