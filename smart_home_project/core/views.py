from django.shortcuts import render
from django.views.generic import ListView
from sensors.models import Sensor
from .models import Device

# Create your views here.


class HomeView(ListView):
    model = Sensor
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['devices'] = Device.objects.all()
        return context
