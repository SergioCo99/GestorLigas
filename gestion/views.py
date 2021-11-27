from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Deporte, Liga, Equipo
import requests

#def index(request):
#	return render(request, 'index.html')

# Lista de Ligas creadas
def index(request):
	ligas = get_list_or_404(Liga.objects.order_by('nombre_liga'))
	context = {'lista_ligas': ligas }
	return render(request, 'index.html', context)

# Lista de equipos que pertenecen a una liga concreta
def listaEquiposLiga(request, nombre_liga):
	equipo = get_list_or_404(Equipo.objects.order_by('nombre_equipo').filter(liga = nombre_liga))
	liga = get_object_or_404(Liga, pk = nombre_liga)
	context = {'liga' : liga, 'lista_equipos_liga': equipo}
	return render(request, 'detailLiga.html', context)

#Lista de equipos NBA por API
def estadisticas(request):
    response = requests.get('http://data.nba.net/10s/prod/v2/2021/teams.json')
    data = response.json()
    teams = data['league']['vegas']
    context = {'teams': teams}
    #print('Teams:', teams)
    return render(request, 'estadisticas.html', context)