from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('liga/<str:nombre_liga>/', views.listaEquiposLiga, name='listaEquiposLiga'),
	path('estadisticas/', views.estadisticas, name='estadisticas'),
]