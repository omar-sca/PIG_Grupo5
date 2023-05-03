from django.urls import path
from usuarios import views

urlpatterns = [
    path('', views.mostrar),
    path('nuevo/', views.nuevo_usuario),
    path('editar/', views.editar_usuario),
]
