from django import forms
import datetime
from django.forms import ValidationError
from django.forms.widgets import DateInput

class ModificarStockForm(forms.Form):
    TIPO_COMPROBANTE = (
        ('', '-Seleccione-'),
        (1, 'Ingreso'),
        (2, 'Egreso'),)
    tipo_comprobante = forms.ChoiceField(
        label='Tipo de comprobante',
        choices=TIPO_COMPROBANTE,
        widget=forms.Select(attrs={'class': 'form-group'})
    )
    numero_comprobante = forms.CharField (label="Número de comprobante", required=True)
    fecha_comprobante = forms.DateField(
        initial=datetime.date.today,
        label="Fecha de comprobante",
        required=True,
        widget=DateInput(attrs={'type': 'date', 'class': 'form-group'})
    )


def numero_valido(valor):
    if valor <= 0:
        raise ValidationError('La cantidad no puede ser menor a 0.')

class IngresarProductoForm(forms.Form):
    nombre_producto = forms.CharField (label="Nombre del producto", required=True)
    fabricante_producto = forms.CharField (label="Nombre del fabricante", required=True)
    stock_producto = forms.IntegerField (label="Cantidad", validators=(numero_valido,))



def direccion_correcta(valor):
    if not any(char.isdigit()for char in valor) or not any(char.isalpha() for char in valor):
        raise ValidationError ('La dirección debe tener calle y altura')


class NuevoFabricanteForm(forms.Form):
    nombre=forms.CharField(label='Nombre', max_length=50)
    direccion=forms.CharField(label='Dirección',validators=(direccion_correcta,))
    telefono=forms.CharField(label='Teléfono')
    mail=forms.EmailField(label='Email')

