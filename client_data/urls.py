from django.urls import path
from django.contrib.auth import views as auth_views
from client_data import views
from .views import Client_Data_List, Client_Data_New, Client_Data_Nuevo, Client_Data_Edit, Client_Data_Editar, Client_Data_Delete, Client_Data_Eliminar, Giro_Negocio_List, Giro_Negocio_Nuevo, Giro_Negocio_Editar, Giro_Negocio_Eliminar, Client_Data_To_Excel_1, Client_Data_To_Excel_2, Giro_Negocio_To_Excel_1, Giro_Negocio_To_Excel_2
from .views import clientes

#JJ 
urlpatterns =[
    path('client_data/', Client_Data_List.as_view(), name='client_data_listado'),
    path('client_data/new', Client_Data_New.as_view(), name='client_data_crear'),
    path('client_data/nuevo', Client_Data_Nuevo.as_view(), name='client_data_nuevo'),
    path('cliente/nuevo', clientes, name='cliente_nuevo'),
    path('client_data/edit/<int:pk>', Client_Data_Edit.as_view(), name='client_data_edit'),
    path('client_data/editar/<int:pk>', Client_Data_Editar.as_view(), name='client_data_editar'),
    path('client_data/delete/<int:pk>', Client_Data_Delete.as_view(), name='client_data_delete'),
    path('client_data/eliminar/<int:pk>', Client_Data_Eliminar.as_view(), name='client_data_eliminar'),
    path('client_data/client_data_to_excel_1', Client_Data_To_Excel_1, name='client_data_to_excel_1'),
    path('client_data/client_data_to_excel_2', Client_Data_To_Excel_2, name='client_data_to_excel_2'),
    path('giro_negocio/', Giro_Negocio_List.as_view(), name='giro_negocio_listado'),
    path('giro_negocio/nuevo', Giro_Negocio_Nuevo.as_view(), name='giro_negocio_nuevo'),
    path('giro_negocio/editar/<int:pk>', Giro_Negocio_Editar.as_view(), name='giro_negocio_editar'),
    path('giro_negocio/eliminar/<int:pk>', Giro_Negocio_Eliminar.as_view(), name='giro_negocio_eliminar'),
    path('giro_negocio/giro_negocio_to_excel_1', Giro_Negocio_To_Excel_1, name='giro_negocio_to_excel_1'),
    path('giro_negocio/giro_negocio_to_excel_2', Giro_Negocio_To_Excel_2, name='giro_negocio_to_excel_2'),
]
