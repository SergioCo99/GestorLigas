from django.db import models

# Create your models here.

class Deporte(models.Model):
	nombre = models.CharField(max_length=50, null=False, primary_key=True)
	descripcion = models.CharField(max_length=1000)
	def __str__(self):
		return self.nombre

class Liga(models.Model):
	nombre = models.CharField(max_length=50, null=False, primary_key=True)
	descripcion = models.CharField(max_length=1000)
	deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
	#imagen = models.ImageField(default= 'default.png', blank = True)
	fecha_creacion = models.DateField()
	#Usuario creador

	def __str__(self):
		return self.nombre

class Equipo(models.Model):
	nombre = models.CharField(max_length=50, null=False, primary_key=True)
	descripcion = models.CharField(max_length=1000)
	liga = models.ForeignKey(Liga, on_delete=models.CASCADE)
	#imagen = models.ImageField(default= 'default.png', blank = True)
	fecha_creacion = models.DateField()
	#Usuario creador

	def __str__(self):
		return self.nombre