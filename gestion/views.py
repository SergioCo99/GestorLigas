from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from ligainfo.models import LigaInfo
from .models import Deporte, Liga, Equipo
from .forms import *
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
	equipo = Equipo.objects.order_by('nombre_equipo').filter(liga = nombre_liga)
	liga = get_object_or_404(Liga, pk = nombre_liga)
	ligainfo = LigaInfo.objects.filter(nameliga = nombre_liga)
	context = {'liga' : liga, 'lista_equipos_liga': equipo, 'ligainfo' : ligainfo}
	return render(request, 'detailLiga.html', context)

#Lista de equipos NBA por API
def estadisticas(request):
    response = requests.get('http://data.nba.net/10s/prod/v2/2021/teams.json')
    data = response.json()
    teams = data['league']['vegas']
    context = {'teams': teams}
    #print('Teams:', teams)
    return render(request, 'estadisticas.html', context)

	
def addEquipo(request):
	form = FormularioEquipo()
	if request.method == 'POST': 
		form = FormularioEquipo(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect('index')
	context = {"form": form}
	return render(request, "crearEquipo.html", context)

def addDeporte(request):
	form = FormularioDeporte()
	if request.method == 'POST': 
		form = FormularioDeporte(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	context = {"form": form}
	return render(request, "crearDeporte.html", context)

def addLiga(request):
	form = FormularioLiga()
	if request.method == 'POST': 
		form = FormularioLiga(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect('index')
	context = {"form": form}
	return render(request, "crearLiga.html", context)

def allstar(request):
	
	return render(request, "allstar.html")