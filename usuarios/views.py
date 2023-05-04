from re import template
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.

def inicio_sesion(request):
    return render(request,"usuarios/inicio_sesion.html")

def mostrar(request):
    return render(request,"usuarios/base_usuarios.html")

def nuevo_usuario(request):
    return render(request,"usuarios/base_usuarios.html")

def editar_usuario(request):
    return render(request,"usuarios/base_usuarios.html")
