import json, asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone
from asgiref.sync import sync_to_async

from spots.models import ChatMessage, Spot


@sync_to_async
def save_message(message, time, user, spot_id):
    spot = Spot.objects.get(pk=spot_id)
    ChatMessage.objects.create(
        text=message,
        time=time,
        user=user,
        spot=spot
    )


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
        task1 = asyncio.ensure_future(save_message(message, now, self.user, self.id))
        task2 = asyncio.ensure_future(self.channel_layer.group_send(
            self.chat_group_name, {
                'type': 'chat_message',
                'message': message,
                'user': self.user.username,
                'datetime': now.isoformat(),
            }
        ))

        # send message to group and save message to db
        await asyncio.wait([task1, task2])

    async def chat_message(self, event):
        """Send message to WS"""
        await self.send(text_data=json.dumps(event))