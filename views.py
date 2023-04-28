from re import template
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.

listaProductos=[
    (1,'prod A','fabricante1',32),
    (2,'prod B','fabricante1',0),
    (3,'prod C','fabricante1',5),
    (4,'prod D','fabricante1',65),
    (5,'prod E','fabricante1',9),
    (6,'prod A','fabricante1',32),
    (7,'prod B','fabricante1',0),
    (8,'prod C','fabricante1',5),
    (9,'prod D','fabricante1',65),
    (10,'prod E','fabricante1',9),
    ]

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

