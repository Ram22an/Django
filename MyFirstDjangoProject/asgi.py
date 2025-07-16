"""
ASGI config for MyFirstDjangoProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyFirstDjangoProject.settings')

application = get_asgi_application()

# it works similar to wsgi but comes with some additional functionality
# asgi stand for Asynchronous server gateway interface



