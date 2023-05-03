from django.urls import path
from productos import views

urlpatterns = [
    path('', views.productos_mostrar),
    path('nuevo/', views.producto_nuevo),
    path('editar/<int:id_prod>/', views.producto_editar, name='editar_producto'),
    
    path('fabricantes/', views.fabricantes_mostrar),
    path('fabricantes/nuevo/', views.fabricante_nuevo),
    path('fabricantes/editar/<int:id_fabr>', views.fabricante_editar, name='editar_fabricante'),

    path('modificar_stock/', views.stock),
    path('facturas/', views.ver_facturas),
]
