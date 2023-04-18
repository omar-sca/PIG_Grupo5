from re import template
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.

listaProductos=[('prod A',32),('prod B',0),('prod C',5),('prod D',65),('prod E',9),('prod A',32),('prod B',0),('prod C',5),('prod D',65),('prod E',9),('prod A',32),('prod B',0),('prod C',5),('prod D',65),('prod E',9)]


def mostrar(request):
    template = loader.get_template('productos/productos.html')
    context={'productos':listaProductos}
    return HttpResponse(template.render(context,request))

def nuevo_producto(request):
    #template = loader.get_template('productos/nuevo.html')
    #context={'':}
    #return HttpResponse(template.render(context,request))
    return render(request,'productos/nuevo.html')

def stock(request):
    #template = loader.get_template('productos/modificar_stock.html')
    #context={'':}
    #return HttpResponse(template.render(context,request))
    return render(request,'productos/modificar_stock.html')

def editar(request,id_prod):
    template = loader.get_template('productos/editar.html')
    context={'id_item':id_prod}
    return HttpResponse(template.render(context,request))

