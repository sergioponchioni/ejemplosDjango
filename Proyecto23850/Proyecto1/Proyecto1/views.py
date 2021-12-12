from django import http
from django.http import HttpResponse
from datetime import datetime, date
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola soy Sergio")

def segundaVista(request):
    return HttpResponse("segunda respuesta")

def dia(request):
    variable = datetime.now()

    return HttpResponse(f"hoy es un gran dia <br>{variable}")

def apellido(request, ape):
    variable = datetime.now()
    return HttpResponse(f"el profe de coder {ape} es muy bueno<br> por lo menos hoy{variable}")

def anio(request, edad):
    today = datetime.now()
    anio = today.year - int(edad)

    return HttpResponse(f"tu anio de nacimiento es  {anio}")

def probandoTemplate(request):
    
    #Envio de variables, siempre se define un diccionario y se agrwega abajo en el contexto, luego con doble llave accedo desde el HTML
    mejorEstudiante = "Ilan Fritzler"
    nota = 8.9
    fecha = datetime.now()
    dicc = {"nombre": mejorEstudiante, "nota":nota, "fecha":fecha}
    
    miHTML = open("C:/Users/Qservices/Documents/Python/GitEjemplos/ejemplosDjango/Proyecto23850/Proyecto1/Proyecto1/Plantillas/template1.html")

    plantilla = Template(miHTML.read())

    miHTML.close()

    miContexto = Context(dicc)

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)
