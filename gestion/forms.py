from django import forms
from .models import Equipo, Deporte, Liga

class FormularioEquipo(forms.ModelForm):
	nombre_equipo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Real Madrid C.F'}))
	descripcion = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Equipo que ha ganado 34 ligas'}))
	imagen = forms.ImageField(max_length=100)

	class Meta: #Declaramos todos los datos asociados al formulario
	
		model = Equipo
		fields = ['nombre_equipo' ,'descripcion','liga', 'imagen']
		widgets = {'liga': forms.Select(attrs={'class':'form-control', 'placeholder': 'Selecciona la liga del equipo'})}

class FormularioDeporte(forms.ModelForm):
	nombre_deporte = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Baloncesto'}))
	descripcion = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Deporte de 5vs5'}))

	class Meta: #Declaramos todos los datos asociados al formulario
	
		model = Deporte
		fields = ['nombre_deporte' ,'descripcion']

class FormularioLiga(forms.ModelForm):
	nombre_liga = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: NBA'}))
	descripcion = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Liga de baloncesto de Norteamerica'}))
	imagen_liga = forms.ImageField(max_length=100)

	class Meta: #Declaramos todos los datos asociados al formulario
	
		model = Liga
		fields = ['nombre_liga' ,'descripcion', 'deporte', 'imagen_liga']
		widgets = {'Deporte': forms.Select(attrs={'class':'form-control', 'placeholder': 'Selecciona el deporte de la liga'})}
