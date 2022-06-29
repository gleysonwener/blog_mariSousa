from django import forms
from django.contrib.auth.models import User


class UsuarioForm(forms.ModelForm):
    model = User
    fields = ['username', 'password']


class UsuarioLogin(forms.Form):
    usuario = forms.CharField(label='Usuário', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    senha = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))