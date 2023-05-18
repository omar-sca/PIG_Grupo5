from django.urls import path
from productos import views


urlpatterns = [
    path('', views.productos_mostrar, name='productos'),
    path('nuevo/', views.producto_nuevo, name='nuevo_producto'),
    path('editar/<int:id_prod>/', views.producto_editar, name='editar_producto'),
    path('fabricantes/', views.FabricantesL.as_view(), name='fabricantes'),
    path('fabricantes/nuevo/', views.fabricante_nuevo, name='nuevo_fabricante'),
    path('fabricantes/editar/<int:id_fabr>', views.fabricante_editar, name='editar_fabricante'),
    path('modificar_stock/', views.stock, name='modificar_stock'),
    path('facturas/', views.ver_facturas),
]
