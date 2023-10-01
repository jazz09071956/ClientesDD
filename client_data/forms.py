from django import forms
from django.http import request
from client_data.models import Cliente, Giro_Negocio
"""
# revisar si se puede usar el widgets para controlar el Textarea de las notas
class Client_Data_Form(forms.Form):
  nombre= forms.CharField(label="Nombre", disabled=True)
"""

TIPO_DOCUMENTO_CHOICES=(("1", "DUI"), ("2", "NIT"), ("3", "PASAPORTE"), ("4", "OTROS"),)

class Client_Data_FormNew(forms.ModelForm):

  class Meta:
    model=Cliente
    fields = ['nombre','tipo_documento','documento_identidad','email',
              'direccion','telefono','numero_registro_contribuyente','giro_negocio' ]
    labels = {'nombre':'Nombre o Razon Social','tipo_documento':'Tipo de Documento Identidad','documento_identidad':'Numero de Documento','email':'Correo Electronico','numero_registro_contribuyente':'Numero de Registro Contribuyente','giro_negocio':'Giro del Negocio'}


  #como se renderiza con bootstrap hay que sobreescribir el metodo init
  def __init__(self, *args, **kwargs):
    super().__init__(*args,**kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({
        'class':'form-control'
      })

class Client_Data_Form(forms.ModelForm):
  # se pueden redifinir los campos de entrada, revisar si valida bien 
  email = forms.EmailField(max_length=254)
  #nombre = forms.TextInput(attrs={"size":5, "title":"Su Nombre"})
  tipo_documento= forms.ChoiceField\
    (label="Tipo de Documento de Identidad", choices=TIPO_DOCUMENTO_CHOICES)
  class Meta:
    model=Cliente
    fields = ['nombre','tipo_documento','documento_identidad','email',
              'direccion','telefono','numero_registro_contribuyente','giro_negocio','nombre_comercial', 'nombre_contacto' ]
    labels = {'nombre':'Nombre o Razon Social','tipo_documento':'Tipo de Documento Identidad','documento_identidad':'Numero de Documento','email':'Correo Electronico','numero_registro_contribuyente':'Numero de Registro Contribuyente','giro_negocio':'Giro del Negocio'}
    #se pueden excluir ciertos campos
    # #exclude = ['modifico', 'modificado', 'creo', 'creado']
    widget={'nombre':forms.TextInput()}
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({
        'class':'form-control'
      })
    
    #self.fields['nombre'].label = 'Usuario'
    #self.fields['nombre'].widget.attrs.update({'class':'primer-grupo'})

  def clean(self):
      try:
          sc = Cliente.objects.get(
              documento_identidad=self.cleaned_data["documento_identidad"].upper()
          )

          if not self.instance.pk:
              print("Documento de Identidad ya existe")
              raise forms.ValidationError("Documento de Identidad Ya Existe")
          elif self.instance.pk!=sc.pk:
              print("Cambio no permitido")
              raise forms.ValidationError("Cambio No Permitido")
      except Cliente.DoesNotExist:
          pass
      return self.cleaned_data

class Giro_Negocio_Form(forms.ModelForm):
  class Meta:
    model=Giro_Negocio
    fields = ['codigo_giro_negocio','nombre_giro_negocio']
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({
        'class':'form-control'
      })
