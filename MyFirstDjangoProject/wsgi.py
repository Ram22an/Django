"""
WSGI config for MyFirstDjangoProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyFirstDjangoProject.settings')

application = get_wsgi_application()


# this is mainly concern with deployment server(like apache, nginx, etc.)
#  wsgi is stand for web server gateway interface
# how the server should interact with web application


