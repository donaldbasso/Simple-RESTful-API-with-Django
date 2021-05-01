from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from myapp.models import Car

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

def get_car(request, car_name):
    if request.method == 'GET':
        try:
            # pouvoir recuperer une image envoyee par le frontend
            #traitement
            #response = json.dumps([{ 'Car': car.name, 'Top Speed': car.top_speed}])
            response = json.dumps({'imageDetected':'http://localhost:8000/media/exp4/car_000001.png', 'boundingBox':[{'class':'car','value':[1230000,1122,2222,22222,222222]},{'class':'stade','value':[1230000,1122,2222,22222,222222]}]})
        except:
            response = json.dumps([{ 'Error': 'No car with that name'}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_car(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        car_name = payload['car_name']
        top_speed = payload['top_speed']
        car = Car(name=car_name, top_speed=top_speed)
        try:
            car.save()
            response = json.dumps([{ 'Success': 'Car added successfully!'}])
        except:
            response = json.dumps([{ 'Error': 'Car could not be added!'}])
    return HttpResponse(response, content_type='text/json')
