from django.urls import path
from productos import views

urlpatterns = [
    path('', views.mostrar),
    path('/nuevo', views.nuevo_producto),
    path('/modificar_stock', views.stock),
    path('/editar/<int:id_prod>', views.editar),
]