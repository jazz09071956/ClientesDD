from django.urls import path
from django.contrib.auth import views as auth_views
from client_sales import views
from .views import Client_Sales_List, Client_Sales_Nuevo, Client_Sales_Editar, Client_Sales_Eliminar
from .views import Sucursal_List, Sucursal_Nuevo, Sucursal_Editar, Sucursal_Eliminar

#JJ 
urlpatterns =[
    path('client_sales/', Client_Sales_List.as_view(), name='client_sales_listado'),
    path('client_sales/nuevo', Client_Sales_Nuevo.as_view(), name='client_sales_nuevo'),
    path('client_sales/editar/<int:pk>', Client_Sales_Editar.as_view(), name='client_sales_editar'),
    path('client_sales/eliminar/<int:pk>', Client_Sales_Eliminar.as_view(), name='client_sales_eliminar'),
    path('sucursal/', Sucursal_List.as_view(), name='sucursal_listado'),
    path('sucursal/nuevo', Sucursal_Nuevo.as_view(), name='sucursal_nuevo'),
    path('sucursal/editar/<int:pk>', Sucursal_Editar.as_view(), name='sucursal_editar'),
    path('sucursal/eliminar/<int:pk>', Sucursal_Eliminar.as_view(), name='sucursal_eliminar'),
]
