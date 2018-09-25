# import os
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dokpo.settings")
#
# application = get_wsgi_application()
#
# from whitenoise import WhiteNoise
# application = WhiteNoise(application, root='/static/')

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dokpo.settings")
application = get_wsgi_application()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'static'))
