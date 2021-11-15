from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
import requests

def index(request):
	return render(request, 'index.html')

def estadisticas(request):
    response = requests.get('http://data.nba.net/10s/prod/v2/2021/teams.json')
    data = response.json()
    teams = data['league']['vegas']
    context = {'teams': teams}
    #print('Teams:', teams)
    return render(request, 'estadisticas.html', context)