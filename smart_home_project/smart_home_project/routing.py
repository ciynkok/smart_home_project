from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from core.consumers import NotificationConsumer
from django.core.asgi import get_asgi_application

websocket_urlpatterns = [
    path('ws/notifications/', NotificationConsumer.as_asgi()),
]
