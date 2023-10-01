from django.db import models
from django.utils import timezone


from client_base.models import TablaBase
from client_data.models import Cliente

#para que devuelva solo la fecha sin la hora
def hoy():
    return timezone.now().date() 


class Sucursal(TablaBase):
    nombre_sucursal=models.CharField(max_length=100,
      unique=True, default='Nombre'
    )
    codigo_sucursal=models.CharField(max_length=10,
      unique=True, default = 'Codigo'
    )
    def __str__(self):
      return '{}'.format(self.nombre_sucursal)
    class Meta:
      verbose_name_plural = "Sucursales"
      verbose_name = "Sucursal"

class Ventas_a_Cliente(TablaBase):
    sucursal_venta=models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    cliente_venta=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_venta=models.DateField(default=hoy)
    documento_venta=models.CharField(max_length=100, blank=True)
    total_venta=models.FloatField(default=0)
    descuento_venta=models.FloatField(default=0)
    def __str__(self):
      return '{}:{}'.format(self.sucursal_venta.nombre,self.documento_venta)
    class Meta:
      verbose_name_plural = "Ventas a Clientes"
      verbose_name = "Venta a Cliente"
      unique_together = ('sucursal_venta','documento_venta')


