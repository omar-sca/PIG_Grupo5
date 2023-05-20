from re import template
from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from productos.forms import NuevoProductoForm, ModificarStockForm,NuevoFabricanteForm,EditarProductoForm
from django.contrib import messages
from django.views.generic import ListView
from productos.models import Fabricante,Items


# Create your views here.

class ProductosMostrar(ListView):
    model = Items
    template_name = 'productos/productos.html'
    context_object_name = 'productos'
    queryset = Items.objects.all().order_by('nombre')

def producto_nuevo(request):
    if request.method == 'POST':
        form_ingresarProducto=NuevoProductoForm(request.POST)
        if form_ingresarProducto.is_valid():
            messages.success(request, 'Nuevo artículo agregado correctamente')
            form_ingresarProducto.save()
            form_ingresarProducto = NuevoProductoForm()
        else:
            messages.warning(request, 'Error en los datos cargados')
    elif request.method=='GET':
        form_ingresarProducto = NuevoProductoForm()
    
    template = loader.get_template('productos/producto_nuevo.html')
    context={'form_nuevoProd':form_ingresarProducto}
    return HttpResponse(template.render(context,request))

def producto_editar(request,id_prod):
    try:
        producto =Items.objects.get(pk=id_prod)
    except Items.DoesNotExist:
        return render(request, '404_admin.html')

    if (request.method == 'POST'):
        form_EditProd = EditarProductoForm(request.POST, instance=producto)
        if form_EditProd.is_valid():
            form_EditProd.save()
            return redirect('productos')
    else:
        form_EditProd = EditarProductoForm(instance=producto)
    return render(request, 'productos/producto_editar.html', {'formEditarProd': form_EditProd})

#def fabricantes_mostrar(request):
#    template = loader.get_template('productos/fabricantes.html')
#    context={'fabricantes':listaFabricantes}
#    return HttpResponse(template.render(context,request))
 
class FabricantesL(ListView):
    model = Fabricante
    template_name = 'productos/fabricantes.html'
    context_object_name = 'fabricantes'
    queryset = Fabricante.objects.all().order_by('nombre')


def fabricante_editar(request,id_fabr):
    template = loader.get_template('productos/fabricante_editar.html')
    context={'id_fabricante':id_fabr}
    return HttpResponse(template.render(context,request))

def fabricante_nuevo(request):
    if request.method =='POST':
        form_nuevo_fab=NuevoFabricanteForm(request.POST)
        if form_nuevo_fab.is_valid():
            messages.success(request, 'Nuevo fabricante agregado')
            form_nuevo_fab.save()
            form_nuevo_fab = NuevoFabricanteForm()

        else:
            messages.warning(request, 'Error en los datos del formulario')
    elif request.method=='GET':
        form_nuevo_fab = NuevoFabricanteForm()

    template = loader.get_template('productos/fabricante_nuevo.html')
    context={'form_nuevo_fab':form_nuevo_fab}
    return HttpResponse(template.render(context,request))

def stock(request):
    template = loader.get_template('productos/modificar_stock.html')
    context={'ModificarStockForm':ModificarStockForm}
    return HttpResponse(template.render(context,request))
    #template = loader.get_template('productos/modificar_stock.html')
    #context={'':}
    #return HttpResponse(template.render(context,request))
    #return render(request,'productos/modificar_stock.html')

def ver_comprobantes(request):
    #template = loader.get_template('productos/facturas.html')
    #context={'':}
    #return HttpResponse(template.render(context,request))
    return render(request,'productos/comprobantes.html')
