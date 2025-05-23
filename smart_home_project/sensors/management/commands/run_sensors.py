from django.core.management.base import BaseCommand
from sensors.tasks import SimulateSensors
import time
import random


class Command(BaseCommand):
    help = 'Simulate sensor data updates'

    def handle(self, *args, **options):
        while True:
            SimulateSensors().simulate_sensors()
            t = random.randint(1, 10)
            time.sleep(t)
