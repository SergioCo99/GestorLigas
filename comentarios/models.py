from django.db import models

# Create your models here.
class Comentario(models.Model):
	comentario = models.CharField(max_length=50, null=False)
