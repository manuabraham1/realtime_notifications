# alerts/models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Alert(models.Model):
    camera_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100)
    api_key = models.CharField(max_length=100)
    chat_id = models.CharField(max_length=100)
    image_path = models.CharField(max_length=255, null=True, blank=True)
    alert_message = models.TextField()

    def __str__(self):
        return self.camera_name

# Signal to send WebSocket update when a new Alert is created
@receiver(post_save, sender=Alert)
def send_alert_update(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'alert_update_group',
        {
            'type': 'alert_update',
            'message': 'New alert added!',
        }
    )
