from django.db import models

# Create your models here.
class Fabricante(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nombre


class Item(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Comprobante(models.Model):
    class Tipo(models.TextChoices):
        INGRESO = 'ING', 'Ingreso'
        EGRESO = 'EGR', 'Egreso'
    
    numero = models.CharField(max_length=20)
    fecha = models.DateField()
    tipo = models.CharField(max_length=3, choices=Tipo.choices, default=Tipo.INGRESO)
    articulos = models.ManyToManyField(Item,through='ComprobanteProducto')

    def __str__(self):
        return self.numero

class ComprobanteProducto(models.Model):
    comprobante = models.ForeignKey(Comprobante, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Item, on_delete=models.CASCADE)
    cantidad = models.IntegerField()