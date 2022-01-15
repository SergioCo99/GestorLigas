from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    username =  forms.CharField(max_length=100, widget=forms.TextInput(
	    attrs={'class': 'form-control ', 'placeholder': 'Tu nombre de usuario...'}))
    email = forms.EmailField(widget=forms.EmailInput(
	    attrs={'class': 'form-control ', 'placeholder': 'ejemplo@ejemplo.com'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
	    attrs={'class': 'form-control ', 'placeholder': 'Tu nombre...'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
	    attrs={'class': 'form-control ', 'placeholder': 'Tu apellido...'}))
    password1 = forms.CharField(widget = forms.PasswordInput(render_value = True, attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(widget = forms.PasswordInput(render_value = True, attrs={'class': 'form-control', 'placeholder': 'Repita contraseña'}))

   
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
