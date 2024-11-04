from django.shortcuts import render
from .models import Materia
# Create your views here.

def inicio_visita(request):
    lasmaterias=Materia.objects.all

    return render(request,"gestionarMateria.html")