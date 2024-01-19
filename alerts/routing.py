# routing.py


from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/alert_update_group/', consumers.AlertUpdateConsumer.as_asgi(), name='alert_update'),    # Add more WebSocket paths if needed
]

