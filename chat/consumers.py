import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        """Join chat"""
        self.id = self.scope['url_route']['kwargs']['spot_id']
        self.chat_group_name = f'chat_{self.id}'
        async_to_sync(self.channel_layer.group_add)(
            self.chat_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        """leave chat"""
        async_to_sync(self.channel_layer.group_discard)(
            self.chat_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        # receive message from WS
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # send message to group
        async_to_sync(self.channel_layer.group_send)(
            self.chat_group_name, {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        """Send message to WS"""
        self.send(text_data=json.dumps(event))