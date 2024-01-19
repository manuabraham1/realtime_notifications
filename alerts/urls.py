from django.urls import path
from .views import trigger_alert, notification_view

urlpatterns = [
    path('trigger_alert/', trigger_alert, name='trigger_alert'),
    path('notifications/', notification_view, name='notifications'),
]