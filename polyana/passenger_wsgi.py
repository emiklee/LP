# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/e/emik90if/polana18.ru/polyana')
sys.path.insert(1, '/home/e/emik90if/polana18.ru/venv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'polyana.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()