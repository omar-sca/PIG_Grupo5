from django.db import models

# Create your models here.
class Fabricante(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.ManufacturerName


class Items(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return self.ItemName

    class Tipo(models.TextChoices):
        INGRESO = 'ING', 'Ingreso'
        EGRESO = 'EGR', 'Egreso'

class Facturas(models.Model):
    class Tipo(models.TextChoices):
        INGRESO = 'ING', 'Ingreso'
        EGRESO = 'EGR', 'Egreso'
    
    numbero = models.CharField(max_length=20)
    fecha = models.DateField()
    tipo = models.CharField(max_length=2, choices=Tipo.choices, default=Tipo.INGRESO)

    def __str__(self):
        return self.InvoiceNumber

class FacturaProducto(models.Model):
    factura = models.ForeignKey(Facturas, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Items, on_delete=models.CASCADE)