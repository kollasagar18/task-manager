import os
import sys

path = '/home/yourusername/task-manager/note_mage'

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'note_mage.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()