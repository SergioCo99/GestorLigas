from pyexpat import model
from django.db.models.base import ModelState
from rest_framework import serializers
from gestion.models import Equipo, models

class EquipoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipo
        fields = '__all__'