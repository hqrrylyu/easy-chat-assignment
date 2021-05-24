"""
ASGI config for easy_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
# flake8: noqa: E402
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")
from django.core.asgi import get_asgi_application

application = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from easy_chat.chat.urls import websocket_urlpatterns as chat_websocket_urlpatterns


application = ProtocolTypeRouter(
    {
        "http": application,
        "websocket": AuthMiddlewareStack(URLRouter(chat_websocket_urlpatterns)),
    }
)
