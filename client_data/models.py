from django.db import models


from client_base.models import TablaBase

class Giro_Negocio(TablaBase):
    nombre_giro_negocio=models.CharField(max_length=200,
      unique=True, default='Giro de Negocio'
    )
    codigo_giro_negocio=models.CharField(max_length=10,
      unique=True, default = 'Codigo de Actividad'
    )
    def __str__(self):
      return '{}'.format(self.nombre_giro_negocio)
    class Meta:
      verbose_name_plural = "Giros de Negocio"
      verbose_name = "Giro de Negocio"


class Cliente(TablaBase):
  nombre=models.CharField(
    max_length=100
  )
  nombre_comercial=models.CharField(
    max_length=100,
    null=True, blank=True
  )
  nombre_contacto=models.CharField(
    max_length=100,
    null=True, blank=True
  )
  direccion=models.CharField(
    max_length=250,
    null=True, blank=True
  )
  tipo_documento=models.CharField(
    max_length=30,
    null=True, blank=True
  )
  documento_identidad=models.CharField(
    max_length=20,
    unique=True
  )
  numero_registro_contribuyente=models.CharField(
    max_length=20,
    null=True, blank=True
  )
  giro_negocio=models.ForeignKey( Giro_Negocio, null=True, blank=True,  on_delete=models.CASCADE)
  telefono=models.CharField(
    max_length=10,
    null=True, blank=True
  )
  email=models.CharField(
    max_length=250,
    null=True, blank=True
  )
  categoria_cliente=models.CharField(
    max_length=5,
    null=True, blank=True
  )
  descuento_autorizado=models.FloatField(default=0)

  def __str__(self):
    return '{}'.format(self.nombre)

  def save(self):
    self.nombre=self.nombre.upper()
    super(Cliente, self).save()

  class Meta:
    verbose_name_plural = "Clientes"

