"""
ASGI config for proyecto project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

# proyecto/asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import inicio.routing  # Importa las rutas de tu aplicación 'inicio'
from inicio import consumers  # Importa tus consumidores de WebSocket

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            inicio.routing.websocket_urlpatterns
        )
    ),
})
