from django.urls import path
from chat import consumers


websocket_urlpatterns = [
    path('ws/chat/<int:spot_id>/', consumers.ChatConsumer),
]
