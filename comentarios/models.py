from django.db import models
from gestion.models import *
from datetime import date, datetime
from django.contrib.auth.models import User
now = datetime.now()
# Create your models here.
# Create your models here.
class Comentario(models.Model):
    usuario = models.CharField(max_length=25)
    liga = models.CharField(max_length=25)
    comentario = models.CharField(max_length=100)
    date = models.DateTimeField(default=now)

    def _str_(self):
        return self.usuario
