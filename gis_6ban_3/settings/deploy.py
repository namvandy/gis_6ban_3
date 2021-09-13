from .base import *

local_env = open(os.path.join(BASE_DIR, '.env'))
env = dict()

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n','')
    start = line.find('=')
    key = line[:start]
    value = line[start+1:]
    env[key] = value
    print(env)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*', '172.16.243.68']



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password1234',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}