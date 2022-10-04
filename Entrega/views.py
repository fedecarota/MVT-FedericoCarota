from django.http import HttpResponse
from datetime import datetime
from django.template import loader

from home.models import Persona


def crear_persona(request, nombre, apellido, edad):
    
    persona = Persona(nombre=nombre, apellido=apellido, edad=edad, fecha_de_alta=datetime.now())
    persona.save()
    
    template = loader.get_template('crear_persona.html')
    template_renderizado = template.render({'persona' : persona})
    
    return HttpResponse(template_renderizado)


def ver_personas(request):
    
    personas = Persona.objects.all()
    
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'personas' : personas})
    
    return HttpResponse(template_renderizado)