from django.db import models

# Create your models here.

class Deporte(models.Model):
	nombre_deporte = models.CharField(max_length=50, null=False, primary_key=True)
	descripcion = models.CharField(max_length=1000)
	def __str__(self):
		return self.nombre_deporte

class Liga(models.Model):
	nombre_liga = models.CharField(max_length=50, null=False, primary_key=True)
	descripcion = models.CharField(max_length=1000)
	deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
	imagen_liga = models.ImageField(default= 'default.png', blank = True)
	fecha_creacion = models.DateField(auto_now_add=True)
	#Usuario creador

	def __str__(self):
		return self.nombre_liga

class Equipo(models.Model):
	nombre_equipo = models.CharField(max_length=50, null=False, primary_key=True)
	descripcion = models.CharField(max_length=1000)
	liga = models.ForeignKey(Liga, on_delete=models.CASCADE)
	#imagen = models.ImageField(default= 'default.png', blank = True)
	fecha_creacion = models.DateField(auto_now_add=True)
	#Usuario creador

	def __str__(self):
		return self.nombre_equipo

class Patata(models.Model):
	nombre_equip = models.CharField(max_length=50, null=False, primary_key=True)
