from django.http import HttpResponse
from django.shortcuts import render

import personas
from personas.models import Persona, Domicilio


# Create your views here.
def bienvenido(request):
    no_pesonas_var = Persona.objects.count()
    personas = Persona.objects.all()
    personas = Persona.objects.order_by('-id')
    no_domicilios_var = Domicilio.objects.count()
    domicilios = Domicilio.objects.all()
    domicilios = Domicilio.objects.order_by('-id')
    return render(request, 'bienvenido.html',
                  {'no_personas': no_pesonas_var, 'personas': personas, 'no_domicilios': no_domicilios_var,
                   'domicilios': domicilios})


def despedirse(request):
    return HttpResponse('hasta pronto')
