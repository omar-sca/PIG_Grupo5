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
from django.views.generic import CreateView, TemplateView,ListView,UpdateView
from usuarios.forms import Nuevo_usuario_form,Editar_usuario_form
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

# Create your views here.


class Nuevo_usuario(PermissionRequiredMixin,CreateView):
    permission_required='auth.add_user'
    model = User
    form_class = Nuevo_usuario_form
    template_name="usuarios/nuevo_usuario.html"
    context_object_name='form'

    def form_valid(self, form):
        form.save()
        form.cleaned_data['grupo'].user_set.add(form.instance)
        return redirect('/usuarios')


class Mostrar(PermissionRequiredMixin,ListView):
    permission_required='auth.view_user'
    model = User
    template_name = 'usuarios/usuarios.html'
    context_object_name = 'usuarios'
    queryset = User.objects.filter(is_staff=False).order_by('username')


@permission_required('auth.change_user')
def editar_usuario(request,id_user):
    try:
        usuario = User.objects.get(pk=id_user)
    except User.DoesNotExist:
        return render(request, '404_admin.html')

    if (request.method == 'POST'):
        form_EditUser = Editar_usuario_form(request.POST)
        # if form_EditUser.is_valid():
        # revisar: setear password, si el form valida las passwords y como cambiar el grupo al que se asocia el usuario 
        #     form_EditUser.cleaned_data['grupo'].user_set.add(user)
        return redirect('usuarios')
    else:
        form_EditUser = Editar_usuario_form()
        pass

    template=loader.get_template('usuarios/editar_usuario.html')
    context={'id_user':id_user,'form':form_EditUser}
    return HttpResponse(template.render(context,request))


@permission_required('auth.delete_user')
def eliminar_usuario(request,id_user):
    try:
        usuario =User.objects.get(pk=id_user)
    except User.DoesNotExist:
        return render(request, '404_admin.html')
    usuario.delete()
    return redirect('mostrar_usuarios')    


def inicio_sesion(request):
    if request.user.is_authenticated:
        return redirect('productos')
    
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
