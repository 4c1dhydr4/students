import os
import dj_database_url

db_from_env = dj_database_url.config()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '%vw%s6x%l$1xh8kn51sh!5%1i@uvk3hy#z2-rjy!00ho!7%8(e'

DEBUG = True

ALLOWED_HOSTS = ['*']

ADMINS = [('Sync Students', 'syncstudents@synapsesystems.tech')]

LOGGING_CONFIG = None

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'class': '',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

LOCAL_APPS = (
    'apps.home',
    'apps.students',
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_APPS = (

)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'syncStudents.urls'

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
                'apps.home.context_processors.user',
            ],
        },
    },
]

WSGI_APPLICATION = 'syncStudents.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'students',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

DATABASES['default'].update(db_from_env)
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collected')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# from django.urls import reverse_lazy
# LOGIN_REDIRECT_URL = reverse_lazy('inicio:index')

# Email
EMAIL_HOST = 'mail.synapsesystems.tech'
EMAIL_HOST_USER = 'syncstudents@synapsesystems.tech'
EMAIL_HOST_PASSWORD = 'DorPa391!'
EMAIL_SUBJECT_PREFIX = 'syncStudents'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True

