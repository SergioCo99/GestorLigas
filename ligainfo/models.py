from django.db import models
from gestion.models import *
# Create your models here.
class LigaInfo(models.Model):
    nameliga = models.CharField(max_length=50, default="a")
    anyocreacion = models.CharField(max_length=50)
    numequipos = models.CharField(max_length=50, default="a")
    maxganador = models.CharField(max_length=50)
    ultimoganador = models.CharField(max_length=50)

    def _str_(self):
        return self.nameliga