# alerts/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Alert

@csrf_exempt
def trigger_alert(request):
    Alert.objects.create(
        camera_name='Test Camera',
        employee_id='123',
        api_key='dummy_api_key',
        chat_id='dummy_chat_id',
        alert_message='New alert added!'
    )
    return HttpResponse("Alert triggered successfully!")

# Signal to send WebSocket update when a new Alert is created
# @receiver(post_save, sender=Alert)
# def send_alert_update(sender, instance, **kwargs):
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         'alert_update_group',
#         {
#             'type': 'alert_update',
#             'message': 'New alert added!',
#         }
#     )

def notification_view(request):
    return render(request, 'notification.html')