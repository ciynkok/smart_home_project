from core.models import Device, Rule
from sensors.models import Sensor
import re


class CheckRules:
    def __init__(self):
        self.rules = Rule.objects.all()
        self.unique_devices = Device.objects.filter(rule__isnull=False).distinct()
        # self.unique_devices = [dev for dev in self.rules.values("device").distinct().device]

    def check(self):
        for rule in self.rules:
            if rule.sensor.sensor_type == 'TMP':
                value1 = ''
                value2 = ''
                for i in rule.value:
                    if bool(re.match(r"^-?\d+(\.\d+)?$", i)):
                        value2 += i
                    elif value1 == '':
                        value1 = value2
                    else:
                        value2 = ''

                if float(value1) < rule.sensor.value < float(value2):
                    rule.device.status = rule.status
                    rule.device.save()

            elif rule.sensor.sensor_type == 'HUM':
                value1 = ''
                value2 = ''
                for i in rule.value:
                    if bool(re.match(r"^-?\d+(\.\d+)?$", i)):
                        value2 += i
                    elif value1 == '':
                        value1 = value2
                    else:
                        value2 = ''

                if float(value1) < rule.sensor.value < float(value2):
                    rule.device.status = rule.status
                    rule.device.save()

            elif rule.sensor.sensor_type == 'MTN':
                if float(rule.value) == rule.sensor.value:
                    rule.device.status = rule.status
                    rule.device.save()
        # for dev in self.unique_devices:
        #     rules = self.rules.filter(device=dev)
        #     change_status = True
        #     for rule in rules:
        #         change_status = change_status and (rule.value == rule.sensor.value)
        #     if change_status:
        #         dev.status = rules.first().status
        #         dev.save()


