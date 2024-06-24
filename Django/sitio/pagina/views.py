from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from .models import Mimodelo
# Create your views here.

def hola_mundo(request):
    return HttpResponse('Hola mundo')

def api_json (request):
    data = [{
        'id':1,
        'nombre':'Alma',
        'edad':17,
        'trabaja':True
    }]
    return JsonResponse(data, safe=False)

def mi_pagina(request):
    template = loader.get_template('pagina.html')
    datos = {
        'nombre' : 'Alma'

    }
    return HttpResponse(template.render(datos,request))

def mi_modelo(request):
    # modelo = Mimodelo(id = 2)
    # modelo.nombre = 'Rosca rellena'
    # modelo.forma = 'Ovalada'
    # modelo.relleno = True
    # modelo.precio = 80.50
    # modelo.save()
    # return HttpResponse('modelo')

    # modelo = Mimodelo()

    data = Mimodelo.objects.all().values
    return JsonResponse(list(data), safe=False)

def react(request):
    template = loader.get_template('react.html')
    return HttpResponse(template.render())




