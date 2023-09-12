from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.models import User
from client_data.models import Cliente
from .forms import  Client_Data_Form, Client_Data_FormNew
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy



class Client_Data_List(generic.ListView):
    model = Cliente
    template_name = "client_data/client_data_listar.html"
    context_object_name = "clientes"
    #para filtrar los clientes hay que sobreescribir el metodo get_queryset
    def get_queryset(self):
        qs = super().get_queryset()
        return qs

class Client_Data_New(generic.CreateView):
    model=Cliente
    template_name="client_data/client_data_formulario.html"
    context_object_name="clientes"
    form_class=Client_Data_FormNew
    # el CreateView requiere un success_url
    success_url=reverse_lazy("client_data_listar")


class Client_Data_Edit(generic.UpdateView):
    model=Cliente
    template_name="client_data/client_data_formulario.html"
    context_object_name="clientes"
    form_class=Client_Data_FormNew
    # el CreateView requiere un success_url
    success_url=reverse_lazy("client_data_listar")
    success_message="Cliente Actualizado Exitosamente"

class Client_Data_Delete(generic.DeleteView):
    model=Cliente
    template_name="client_data/client_data_eliminar.html"
    context_object_name="clientes"
    success_url=reverse_lazy("client_data_listar")
