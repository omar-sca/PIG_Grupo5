from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User,Group


class Nuevo_usuario_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2',]
    
    username = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Username'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password Again'}))
    grupo=forms.ModelChoiceField(queryset=Group.objects.all().order_by('name'))


class Editar_usuario_form(forms.Form):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password Again'}))
    grupo=forms.ModelChoiceField(queryset=Group.objects.all().order_by('name'))
