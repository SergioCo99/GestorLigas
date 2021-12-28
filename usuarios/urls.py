from django.urls import path
from django.conf.urls import include
from . import views
from .views import *

urlpatterns = [
    path('login/', views.Login, name='Login'),
    path('logout/', views.logout_view, name='Logout'),
    path('registro/', UserRegisterView.as_view(), name='Registro'),
    path('editarusuario/', UserEditView.as_view(), name='EditarUsuario'),

]