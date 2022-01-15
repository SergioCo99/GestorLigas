from django.shortcuts import render
from django.contrib.auth  import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
# Create your views here.

def Login(request): 
    if request.method == 'POST':
        usuario=request.POST.get('usuario')
        contra=request.POST.get('contra')
        user = authenticate( request, username=usuario, password=contra)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

class UserRegisterView(generic.CreateView):
		form_class = SignUpForm
		template_name = 'usuarios/registro.html'
		success_url = reverse_lazy('index')