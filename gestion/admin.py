from django.contrib import admin
from .models import Deporte, Liga, Equipo
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Deporte)
admin.site.register(Liga)
admin.site.register(Equipo)
