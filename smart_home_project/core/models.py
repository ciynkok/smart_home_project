from django.db import models
from sensors.models import Sensor

# Create your models here.


class Device(models.Model):
    DEVICES_TYPES = [('LMP', 'Smart lamp'),
                     ('SCT', 'Smart socket'),
                     ('DMR', 'Dimmer'),
                     ('CND', 'Conditioner'),
                     ('HTR', 'Heater'),
                     ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=DEVICES_TYPES)
    status = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.name} type:{self.type} status:{self.status}'


class Rule(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    status = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
