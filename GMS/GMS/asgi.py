"""
ASGI config for GMS project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GMS.settings')

application = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
import main.routing
# application = get_asgi_application()
application=ProtocolTypeRouter({
	'websocket':URLRouter(main.routing.ws_patterns)
})