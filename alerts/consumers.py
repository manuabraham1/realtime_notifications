# alerts/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AlertUpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connected')
        self.group_name = 'alert_update_group'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)


    async def alert_update(self, event):
        print('alert_update function called')
        message = event['message']

        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
