import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Join chat"""
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['spot_id']
        self.chat_group_name = f'chat_{self.id}'
        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        """leave chat"""
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # receive message from WS
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        now = timezone.now()

        # send message to group
        await self.channel_layer.group_send(
            self.chat_group_name, {
                'type': 'chat_message',
                'message': message,
                'user': self.user.username,
                'datetime': now.isoformat(),
            }
        )

    async def chat_message(self, event):
        """Send message to WS"""
        await self.send(text_data=json.dumps(event))