from re import template
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect


# Create your views here.

#def inicio_sesion(request):
#    return render(request,"usuarios/inicio_sesion.html")

def mostrar(request):
    return render(request,"usuarios/base_usuarios.html")

def nuevo_usuario(request):
    return render(request,"usuarios/base_usuarios.html")

def editar_usuario(request):
    return render(request,"usuarios/base_usuarios.html")

def inicio_sesion(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            nxt = request.GET.get("next", None)
            if nxt is None:
                return redirect('productos')
            else:
                return redirect(nxt)
        else:
            messages.warning(request, f'Los datos ingresados son incorrectos.')
    form = AuthenticationForm()
    return render(request, 'usuarios/inicio_sesion.html', {'form': form, 'title': 'Log in'})
