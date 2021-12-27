import os, sys
sys.path.append('/home/habilidade/apps_wsgi')
sys.path.append('/home/habilidade/apps_wsgi/djagpy')
os.environ['PYTHON_EGG_CACHE'] = '/home/habilidade/apps_wsgi/.python-eggs'
os.environ['DJANGO_SETTINGS_MODULE'] = 'djagpy.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
