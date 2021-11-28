from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('liga/<str:nombre_liga>/', views.listaEquiposLiga, name='listaEquiposLiga'),
	path('estadisticas/', views.estadisticas, name='estadisticas'),
	path('guardarEquipo/', views.addEquipo, name='guardarEquipo'),
	path('guardarDeporte/', views.addDeporte, name='guardarDeporte'),
	path('guardarLiga/', views.addLiga, name='guardarLiga'),

]