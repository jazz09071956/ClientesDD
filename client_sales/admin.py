from django.contrib import admin
#from django.contrib.auth.models import User

from .models import Sucursal, Ventas_a_Cliente

class SucursalAdmin(admin.ModelAdmin):
    model = Sucursal
    list_display = ('id', 'nombre_sucursal', 'codigo_sucursal')
    list_filter = ( 'nombre_sucursal', 'codigo_sucursal')
    list_display_links = ('id', 'nombre_sucursal', 'codigo_sucursal')
    search_fields = ('nombre_sucursal', 'codigo_sucursal')
    list_per_page = 10

admin.site.register(Sucursal, SucursalAdmin)

class Ventas_a_ClienteAdmin(admin.ModelAdmin):
    model = Ventas_a_Cliente
    list_display = ('sucursal_venta', 'cliente_venta', 'fecha_venta','documento_venta','total_venta','descuento_venta')
    list_filter = ( 'sucursal_venta', 'cliente_venta', 'fecha_venta')
    list_display_links = ('sucursal_venta', 'cliente_venta', 'fecha_venta','documento_venta','total_venta','descuento_venta')
    search_fields = ('sucursal_venta', 'cliente_venta', 'fecha_venta','documento_venta','total_venta','descuento_venta')
    list_per_page = 10


admin.site.register(Ventas_a_Cliente, Ventas_a_ClienteAdmin)

