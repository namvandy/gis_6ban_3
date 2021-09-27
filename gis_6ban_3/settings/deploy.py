from .base import *



def read_secret(secret_name):
    # 파일 경로를 알고 있다. -> /run/secrets/DJANGO_SECRET_KEY
    file = open('/run/secrets/'+secret_name)
    secret = file.read()
    secret = secret.lstrip().rstrip()
    file.close()
    return secret


SECRET_KEY =read_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*', '172.16.243.68']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': read_secret('MARIADB_USER'),
        'PASSWORD': read_secret('MARIADB_PASSWORD'),
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}