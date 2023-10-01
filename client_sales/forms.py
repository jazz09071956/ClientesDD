from django import forms
from django.http import request
from client_data.models import Cliente
from client_sales.models import Ventas_a_Cliente, Sucursal

class Client_Sales_Form(forms.ModelForm):
  fecha_venta = forms.DateInput(format='%Y-%m-%d')
  #fecha_venta = forms.DateField(
    #widget=forms.DateInput(format='%Y-%m-%d'),input_formats=['%Y-%m-%d']
  #)
  class Meta:
    model=Ventas_a_Cliente
    fields = ['sucursal_venta','cliente_venta','fecha_venta','documento_venta','total_venta',
              'descuento_venta' ]
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({
        'class':'form-control'
      })
      self.fields['fecha_venta'].widget.attrs['readonly'] = True

class Sucursal_Form(forms.ModelForm):
  class Meta:
    model=Sucursal
    fields = ['nombre_sucursal','codigo_sucursal']
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({
        'class':'form-control'
      })
