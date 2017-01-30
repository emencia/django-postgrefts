
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgrefts',
        'USER': "postgrefts",
        'PASSWORD': "postgrefts",
        'HOST': '127.0.0.1',
        'PORT': '5434',
    },
}

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'easy_thumbnails',
    'sqlparse',
    'postgrefts',
    'tests',
)

MIDDLEWARE = []

ROOT_URLCONF = 'tests.urls'

USE_TZ = True

SECRET_KEY = 'foobar'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
}]


STATIC_URL = '/static/'

