from django.http import HttpResponse
from django.shortcuts import render

from demo.models import Car


# Create your views here.
def create_car(request):
    car = Car(brand='demo', model='demo', color='demo')
    car.save()
    return HttpResponse(f'New car unlocked: {car.brand}, {car.model}')
