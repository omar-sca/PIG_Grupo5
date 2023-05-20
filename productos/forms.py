from django import forms
import datetime
import re
from django.forms import ValidationError
from django.forms.widgets import DateInput
from productos.models import Fabricante,Items


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


class NuevoProductoForm(forms.ModelForm):
    class Meta:
        model= Items
        fields = ['nombre', 'fabricante', 'stock']
    nombre = forms.CharField (label="Nombre del producto", required=True)
    stock = forms.IntegerField (label="Cantidad", validators=(numero_valido,))


class EditarProductoForm(forms.ModelForm):
    class Meta:
        model= Items
        fields = ['nombre', 'fabricante']


def direccion_correcta(valor):
    if not any(char.isdigit()for char in valor) or not any(char.isalpha() for char in valor):
        raise ValidationError ('La dirección debe tener calle y altura')

def telefono_correcto(valor):
    patron = r'^\d{2}-\d{8}$'
    if not re.match(patron, valor):
        raise forms.ValidationError('El número de teléfono debe cumplir el siguiente formato: 01-12345678')


class NuevoFabricanteForm(forms.ModelForm):
    class Meta:
        model= Fabricante
        fields = ['nombre', 'direccion', 'telefono', 'email']
    nombre=forms.CharField(label='Nombre', max_length=50)
    direccion=forms.CharField(label='Dirección',validators=(direccion_correcta,))
    telefono=forms.CharField(label='Teléfono', validators=(telefono_correcto,))
    email=forms.EmailField(label='Email')

