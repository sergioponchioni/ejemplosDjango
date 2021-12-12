"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#Importar las vistas
from Proyecto1.views import saludo, segundaVista, dia, apellido, anio, probandoTemplate

urlpatterns = [
    path('admin/', admin.site.urls),

    #generar las urls
    path("saludo/", saludo),
    path("index2/", segundaVista),
    path("fecha/", dia), 
    path("apellido/<ape>", apellido),
    path("anio/<edad>", anio),
    path("primerTemplate/", probandoTemplate),
]