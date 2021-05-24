import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from easy_chat.chat.models import Message


class ChatConsumer(WebsocketConsumer):
    _group_name = "chat"

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(self._group_name, self.channel_name)
        self.accept()
        self._send_messages(Message.objects.all())

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self._group_name, self.channel_name)

    def receive(self, text_data):
        message = json.loads(text_data)
        message = Message.objects.create(username=message["username"], text=message["text"])

        async_to_sync(self.channel_layer.group_send)(
            self._group_name, {"type": "send_messages", "messages": [message]}
        )

    def send_messages(self, event):
        messages = event["messages"]
        self._send_messages(messages)

    def _send_messages(self, messages):
        self.send(
            text_data=json.dumps(
                {
                    "type": "messages",
                    "messages": [message.to_dict() for message in messages],
                }
            )
        )
