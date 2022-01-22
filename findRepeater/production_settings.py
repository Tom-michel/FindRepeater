import dj_database_url
from .settings import *


DEBUG = False

TEMPLATE_DEBUG = False



ALLOWED_HOSTS = ['findrepeater.herokuapp.com']

DATABASES['default'] = dj_database_url.config()

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'