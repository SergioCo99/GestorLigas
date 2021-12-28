from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    username =  forms.CharField(max_length=100, widget=forms.TextInput(
	    attrs={'class': 'form-control ', 'placeholder': 'Set your username...'}))
    email = forms.EmailField(widget=forms.EmailInput(
	    attrs={'class': 'form-control '}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
	    attrs={'class': 'form-control ', 'placeholder': 'Set your first name...'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
	    attrs={'class': 'form-control ', 'placeholder': 'Set your last name...'}))
    password1 = forms.CharField(widget = forms.PasswordInput(render_value = True, attrs={'class': 'form-control', 'placeholder': 'Your password'}))
    password2 = forms.CharField(widget = forms.PasswordInput(render_value = True, attrs={'class': 'form-control', 'placeholder': 'Your password'}))

   
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class EditProfileForm(UserChangeForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control '}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Set your first name...'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Set your last name...'}))
	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control '}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')