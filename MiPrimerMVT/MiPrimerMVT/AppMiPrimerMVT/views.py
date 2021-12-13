from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
#Paso 1 Cargadores
from django.template import loader

from AppMiPrimerMVT.models import Familiar

# Create your views here.
def familiares(request):
    
    #Envio de variables, siempre se define un diccionario y se agrwega abajo en el contexto, luego con doble llave accedo desde el HTML
    dicc = {'familiares': Familiar.objects.all(), 'cantidad': Familiar.objects.all().count()}
    
    #Paso 3  
    plantilla = loader.get_template("template1.html")

    #Paso 4 y 5
    documento = plantilla.render(dicc)

    return HttpResponse(documento)
