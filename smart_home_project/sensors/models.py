from django.db import models

# Create your models here.


class Sensor(models.Model):
    SENSOR_TYPES = [('TMP', 'Temperature'),
                    ('HUM', 'Humidity'),
                    ('MTN', 'Motion')]

    name = models.CharField(max_length=100)
    sensor_type = models.CharField(max_length=20, choices=SENSOR_TYPES)
    value = models.FloatField(default=0.0)
    time_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
