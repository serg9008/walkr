import os
import sys

sys.path.append('/var/www/walkr/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'walkr_backend.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
