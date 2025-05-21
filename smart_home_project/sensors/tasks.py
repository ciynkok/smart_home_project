import random
from django.utils import timezone
from .models import Sensor

def simulate_sensors():
    sensors = Sensor.objects.all()

    for sensor in sensors:
        if sensor.sensor_type == 'TMP':
            sensor.value = round(random.uniform(18, 30), 1)
        elif sensor.sensor_type == 'HUM':
            sensor.value = round(random.uniform(40, 70), 1)
        elif sensor.sensor_type == 'MTN':
            sensor.value = random.choice([0, 1])

        sensor.save()

