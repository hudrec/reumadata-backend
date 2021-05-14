from .base import *  # noqa

DEBUG = True

SECRET_KEY = '9$a^(gj$)guq@69yhw4-v6qmzdxvgge*s$-waqtqrg*1pcrxum'


ALLOWED_HOSTS = ['localhost']

REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] += [
    'rest_framework.authentication.SessionAuthentication',
]