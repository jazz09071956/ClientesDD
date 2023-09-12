from django.urls import path
from django.contrib.auth import views as auth_views
from client_data import views
from .views import Client_Data_List, Client_Data_New, Client_Data_Edit, Client_Data_Delete

#JJ 
urlpatterns =[
    path('client_data/', Client_Data_List.as_view(), name='client_data_listar'),
    path('client_data/new', Client_Data_New.as_view(), name='client_data_crear'),
    path('client_data/edit/<int:pk>', Client_Data_Edit.as_view(), name='client_data_editar'),
    path('client_data/delete/<int:pk>', Client_Data_Delete.as_view(), name='client_data_eliminar'),
]
