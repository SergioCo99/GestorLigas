from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from gestion.models import *
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def EquipoDetail(request):
	
   
    equipo_request = Equipo.objects.all()
    serializer = EquipoSerializer(equipo_request, many=True)

    return Response(serializer.data)