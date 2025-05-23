from ..core.models import Device, Rule
from ..sensors.models import Sensor


class CheckRules:
    def __init__(self):
        self.rules = Rule.objects.all()


