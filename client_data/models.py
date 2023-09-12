from django.db import models


from client_base.models import TablaBase

class Cliente(TablaBase):
  nombre=models.CharField(
    max_length=100,
    unique=True
  )
  direccion=models.CharField(
    max_length=250,
    null=True, blank=True
  )
  nit=models.CharField(
    max_length=20
  )
  telefono=models.CharField(
    max_length=10,
    null=True, blank=True
  )
  email=models.CharField(
    max_length=250,
    null=True, blank=True
  )
  def __str__(self):
    return '{}'.format(self.nombre)

  def save(self):
    self.nombre=self.nombre.upper()
    super(Cliente, self).save()

  class Meta:
    verbose_name_plural = "Clientes"

