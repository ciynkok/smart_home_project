from django.apps import AppConfig
from django.db.models.signals import post_save


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from sensors.models import Sensor
        from . import signals

        post_save.connect(signals.device_changed, sender=Sensor)
