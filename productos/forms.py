from django import forms
import datetime

class ModificarStockForm(forms.Form):
    TIPO_COMPROBANTE = (
        ('', '-Seleccione-'),
        (1, 'Ingreso'),
        (2, 'Egreso'),)
    tipo_comprobante = forms.ChoiceField(
        label='Tipo de comprobante',
        choices=TIPO_COMPROBANTE,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    numero_comprobante = forms.CharField (label="Numero de comprobante", required=True)
    fecha_comprobante = forms.DateField(initial=datetime.date.today, label="Fecha de comprobante", required=True)


class IngresarProductoForm(forms.Form):
    nombre_producto = forms.CharField (label="Nombre del producto", required=True)
    fabricante_producto = forms.CharField (label="Nombre del fabricante", required=True)
    stock_producto = forms.IntegerField (label="Cantidad", required=True)

