from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.models import User
from client_data.models import Cliente
from client_sales.models import Ventas_a_Cliente, Sucursal
from .forms import  Client_Sales_Form, Sucursal_Form
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

#este mixin se puede incluir en la aplicacion base
class MixinFormInvalid():
    def form_invalid(self, form):
        response = super().form_invalid(form)
        #if self.request.is_ajax(): #deprecated
        #if self.request.headers.get('x-requested-with') == 'XMLHttRequest':
        if self.request.accepts("application/json"):
            return JsonResponse(form.errors,status=400)
        else:
            return response

class Client_Sales_List(generic.ListView):
    model = Ventas_a_Cliente
    template_name = "client_sales/client_sales_listado.html"
    context_object_name = "ventas_a_clientes"
    #para filtrar las ventas_a_cliente hay que sobreescribir el metodo get_queryset
    def get_queryset(self):
        qs = super().get_queryset()
        return qs


class Client_Sales_Nuevo(SuccessMessageMixin, MixinFormInvalid, generic.CreateView):
    model=Ventas_a_Cliente
    template_name="client_sales/client_sales_form.html"
    context_object_name="ventas_a_clientes"
    form_class=Client_Sales_Form
    success_url=reverse_lazy("client_sales_listado")
    success_message="Cliente Agregado Correctamente"
    """
    def form_valid(self, form):
        form.instance.creo= self.request.user
        print(self.request.user.id)
        return super().form_valid(form)
    """

class Client_Sales_Editar(SuccessMessageMixin, MixinFormInvalid, generic.UpdateView):
    model=Ventas_a_Cliente
    template_name="client_sales/client_sales_form.html"
    context_object_name="ventas_a_clientes"
    form_class=Client_Sales_Form
    # el CreateView requiere un success_url
    success_url=reverse_lazy("client_sales_listado")
    success_message="Cliente Actualizado Exitosamente"

class Client_Sales_Eliminar(generic.DeleteView):
    model=Ventas_a_Cliente
    template_name="client_sales/client_sales_eliminar.html"
    context_object_name="ventas_a_clientes"
    success_url=reverse_lazy("client_sales_listado")
#sucursales

class Sucursal_List(generic.ListView):
    model = Sucursal
    template_name = "client_sales/sucursal_listado.html"
    context_object_name = "sucursales"
    #para filtrar las ventas_a_cliente hay que sobreescribir el metodo get_queryset
    def get_queryset(self):
        qs = super().get_queryset()
        return qs


class Sucursal_Nuevo(SuccessMessageMixin, MixinFormInvalid, generic.CreateView):
    model=Sucursal
    template_name="client_sales/sucursal_form.html"
    context_object_name="sucursales"
    form_class=Sucursal_Form
    success_url=reverse_lazy("sucursal_listado")
    success_message="Sucursal Agregada Correctamente"

class Sucursal_Editar(SuccessMessageMixin, MixinFormInvalid, generic.UpdateView):
    model=Sucursal
    template_name="client_sales/sucursal_form.html"
    context_object_name="sucursales"
    form_class=Sucursal_Form
    success_url=reverse_lazy("sucursal_listado")
    success_message="Sucursal Actualizada Exitosamente"

class Sucursal_Eliminar(generic.DeleteView):
    model=Sucursal
    template_name="client_sales/sucursal_eliminar.html"
    context_object_name="sucursales"
    success_url=reverse_lazy("sucursal_listado")
