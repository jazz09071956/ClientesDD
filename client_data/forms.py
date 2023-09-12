from django import forms
from django.http import request
from client_data.models import Cliente

# revisar si se puede usar el widgets para controlar el Textarea de las notas
class Client_Data_Form(forms.Form):
  nombre= forms.CharField(label="Nombre", disabled=True)

class Client_Data_FormNew(forms.ModelForm):
 
  class Meta:
    model=Cliente
    fields = ['nombre','nit','email','direccion','telefono' ]

  #como se renderiza con bootstrap hay que sobreescribir el metodo init
  def __init__(self, *args, **kwargs):
    super().__init__(*args,**kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({
        'class':'form-control'
      })

