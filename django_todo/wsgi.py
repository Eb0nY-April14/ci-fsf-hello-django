"""
WSGI config for django_todo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

# 'wsgi.py' contains the code that allows our web server to 
# communicate with our Python application.

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_todo.settings')

application = get_wsgi_application()
