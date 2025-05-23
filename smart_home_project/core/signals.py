from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from sensors.models import Sensor
import logging
from automation.rules import CheckRules
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


logger = logging.getLogger(__name__)


@receiver(post_save, sender=Sensor)
def device_changed(sender, instance, created, **kwargs):
    action = "created" if created else "updated"
    logger.info(f"Sensor {instance.name} was {action}. Current value: {instance.value}")
    # channel_layer = get_channel_layer()
    #
    # async_to_sync(channel_layer.group_send)(
    #     "notifications",  # Имя группы должно совпадать с consumer
    #     {
    #         "type": "device.notification",  # Должно соответствовать методу в consumer
    #         "message": {
    #             "event": "device_updated",
    #             "device_id": instance.id,
    #             "device_name": instance.name,
    #             "is_on": instance.is_on,
    #             "status": instance.status,
    #             "created": created
    #         }
    #     }
    # )
    # print("Signal triggered for device update")
    CheckRules().check()


