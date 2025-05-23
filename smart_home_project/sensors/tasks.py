import random
# from django.utils import timezone
from .models import Sensor


class SimulateSensors:
    def __init__(self):
        self.sensors = Sensor.objects.all()
        random_n = random.randrange(self.sensors.count())
        for i in range(random_n):
            self.sensors = self.sensors.exclude(id=random.randrange(self.sensors.count()))

    def simulate_sensors(self):
        for sensor in self.sensors:
            if sensor.sensor_type == 'TMP':
                sensor.value = round(random.uniform(5, 40), 1)
            elif sensor.sensor_type == 'HUM':
                sensor.value = round(random.uniform(40, 70), 1)
            elif sensor.sensor_type == 'MTN':
                sensor.value = random.choice([1, 0])
            sensor.save()
            print(sensor.value)
