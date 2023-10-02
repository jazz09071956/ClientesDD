from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.models import User
from client_data.models import Cliente, Giro_Negocio
from .forms import  Client_Data_Form, Client_Data_FormNew, Giro_Negocio_Form
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from io import BytesIO
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell



class MixinFormInvalid():
    def form_invalid(self, form):
        response = super().form_invalid(form)
        #if self.request.is_ajax():
        #if self.request.headers.get('x-requested-with') == 'XMLHttRequest':
        if self.request.accepts("application/json"):
            return JsonResponse(form.errors,status=400)
        else:
            return response

class Client_Data_List(generic.ListView):
    model = Cliente
    template_name = "client_data/client_data_listado.html"
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

class Client_Data_Nuevo(SuccessMessageMixin, MixinFormInvalid, generic.CreateView):
    model=Cliente
    template_name="client_data/client_data_form.html"
    context_object_name="clientes"
    form_class=Client_Data_Form
    success_url=reverse_lazy("client_data_listado")
    success_message="Cliente Agregado Correctamente"
    """
    def form_valid(self, form):
        form.instance.creo= self.request.user
        print(self.request.user.id)
        return super().form_valid(form)
    """
    # revisar en la documentacion oficial de Django [Form handling with class-based views]
    """
    para no repetir codigo hay que crear un Mixin
    def form_invalid(self,form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors,status=400)
        else:
            return response
    """
# En caso de que el formulario no sea tan estandard
def clientes(request,id=None):
    template_name="client_data/clientes.html"
    giros_negocio = Giro_Negocio.objects.filter(estado=True)
    
    if request.method == "GET":
        cliente = Cliente.objects.filter(pk=id).first()
        if not cliente:
            client = {
                'id':0,
                'nombre':'',
                'nombre_comercial':'',
                'nombre_contacto':'',
                'direcccion':'',
                'tipo_documento':'',
                'documento_identidad':'',
                'numero_registro_contribuyente':'',
                'tipo_documento':'',
                'giro_negocio':'',
                'email':'',
                'categoria_cliente':'',
                'descuento_autorizado':''
            }
        else:
            encabezado = {
                'id':cliente.id,
                'nombre':cliente.nombre,
                'nombre_comercial':cliente.nombre_comercial,
                'nombre_contacto':cliente.nombre_contacto,
                'direcccion':cliente.direccion,
                'tipo_documento':cliente.tipo_documento,
                'documento_identidad':cliente.documento_identidad,
                'numero_registro_contribuyente':cliente.numero_registro_contribuyente,
                'tipo_documento':cliente.tipo_documento,
                'giro_negocio':cliente.giro_negocio,
                'email':cliente.email,
                'categoria_cliente':cliente.categoria_cliente,
                'descuento_autorizado':cliente.descuento_autorizado
            }

        contexto = {"cliente":client,"giros_negocio":giros_negocio}
        return render(request,template_name,contexto)
"""
    if request.method == "POST":
        giro = request.POST.get("cliente_giro_negocio")
        giro_negocio=Giro_Negocio.objects.get(pk=giro)

        if not id:
            cliente = Cliente(
                cliente = cli,
                fecha = fecha
            )
            if enc:
                enc.save()
                id = enc.id
        else:
            enc = FacturaEnca.objects.filter(pk=id).first()
            if enc:
                enc.cliente = cli
                enc.save()

        if not id:
            messages.error(request,'No se puede Continuar No se Detecta No. de Factura')
            return redirect("ventas:factura_list")
        
        codigo = request.POST.get("codigo")
        cantidad = request.POST.get("cantidad")
        precio = request.POST.get("precio")
        s_total = request.POST.get("sub_total_detalle")
        descuento = request.POST.get("descuento_detalle")
        total = request.POST.get("total_detalle")

        prod = Producto.objects.get(codigo=codigo)
        det = FacturaDeta(
            factura = enc,
            producto = prod,
            cantidad = cantidad,
            precio = precio,
            sub_total = s_total,
            descuento = descuento,
            total = total
        )
        
        if det:
            det.save()
        
        return redirect("ventas:factura_edit",id=id)

    return render(request,template_name,contexto)
"""    



class Client_Data_Edit(generic.UpdateView):
    model=Cliente
    template_name="client_data/client_data_formulario.html"
    context_object_name="clientes"
    form_class=Client_Data_FormNew
    # el CreateView requiere un success_url
    success_url=reverse_lazy("client_data_listar")
    success_message="Cliente Actualizado Exitosamente"

class Client_Data_Editar(SuccessMessageMixin, MixinFormInvalid, generic.UpdateView):
    model=Cliente
    template_name="client_data/client_data_form.html"
    context_object_name="clientes"
    form_class=Client_Data_Form
    # el CreateView requiere un success_url
    success_url=reverse_lazy("client_data_listado")
    success_message="Cliente Actualizado Exitosamente"

class Client_Data_Delete(generic.DeleteView):
    model=Cliente
    template_name="client_data/client_data_delete.html"
    context_object_name="clientes"
    success_url=reverse_lazy("client_data_listar")

class Client_Data_Eliminar(generic.DeleteView):
    model=Cliente
    template_name="client_data/client_data_eliminar.html"
    context_object_name="clientes"
    success_url=reverse_lazy("client_data_listado")

class Giro_Negocio_List(generic.ListView):
    model = Giro_Negocio
    template_name = "client_data/giro_negocio_listado.html"
    context_object_name = "giros_negocio"
    #para filtrar las ventas_a_cliente hay que sobreescribir el metodo get_queryset
    def get_queryset(self):
        qs = super().get_queryset()
        return qs


class Giro_Negocio_Nuevo(SuccessMessageMixin, MixinFormInvalid, generic.CreateView):
    model=Giro_Negocio
    template_name="client_data/giro_negocio_form.html"
    context_object_name="giros_negocio"
    form_class=Giro_Negocio_Form
    success_url=reverse_lazy("giro_negocio_listado")
    success_message="Giro Negocio Agregado Correctamente"

class Giro_Negocio_Editar(SuccessMessageMixin, MixinFormInvalid, generic.UpdateView):
    model=Giro_Negocio
    template_name="client_data/giro_negocio_form.html"
    context_object_name="giros_negocio"
    form_class=Giro_Negocio_Form
    success_url=reverse_lazy("giro_negocio_listado")
    success_message="Giro Negocio Actualizado Exitosamente"

class Giro_Negocio_Eliminar(generic.DeleteView):
    model=Giro_Negocio
    template_name="client_data/giro_negocio_eliminar.html"
    context_object_name="giros_negocio"
    success_url=reverse_lazy("giro_negocio_listado")

class Client_Data_To_Pdf(generic.DeleteView):
    model=Cliente
    template_name="client_data/client_data_to_pdf.html"
    context_object_name="clientes"
    success_url=reverse_lazy("client_data_listado")

def Client_Data_To_Excel_1(request):
    context = {
        'archivo': 'DatosCleiente',
    }

    return render(request, 'client_data/client_data_to_excel_1.html', {'context': context})


def Client_Data_To_Excel_2(request):

    queryset_list = Cliente.objects.values('nombre','tipo_documento','documento_identidad','email','direccion','telefono','numero_registro_contribuyente','giro_negocio','nombre_comercial','nombre_contacto')
    #contenido del campo archivo
    if 'archivo' in request.GET:
        archivo = request.GET['archivo']

    # Crear un objeto (object) para crear archivos en memoria
    temp_file = BytesIO()

    # Empezar un libro (workbook)
    workbook = xlsxwriter.Workbook(temp_file)
    worksheet = workbook.add_worksheet()
    
    # Prepararar los datos a escribirse
    data = []
    for cliente in queryset_list:
        nombre=cliente['nombre']
        tipo_documento=cliente['tipo_documento']
        documento_identidad=cliente['documento_identidad']
        email=cliente['email']
        direccion=cliente['direccion']
        telefono=cliente['telefono']
        numero_registro_contribuyente=cliente['numero_registro_contribuyente']
        giro_negocio=cliente['giro_negocio']
        nombre_comercial=cliente['nombre_comercial']
        nombre_contacto=cliente['nombre_contacto']
        #nombre de giro
        if giro_negocio:
            giro = Giro_Negocio.objects.filter(id=giro_negocio).first()
            nombregiro=giro.nombre_giro_negocio
        else:
            nombregiro='Sin Giro de Negocio'

        #nombre de Tipo de documento
        nombretipo='Sin Tipo de Documento'

        match tipo_documento:
            case '1':
                nombretipo = "DUI"
            case '2':
                nombretipo = "NIT"
            case '3':
                nombretipo = "PASAPORTE"
            case '4':
                nombretipo = "OTROS"

        data.append([nombre, nombretipo, documento_identidad, email, direccion, telefono, numero_registro_contribuyente, nombregiro, nombre_comercial, nombre_contacto])


    # Escribir los encabezados de la hoja de trabajo (linea 1)
    worksheet.write(0,0,'Nombre')
    worksheet.write(0,1,'Tipo de documento')
    worksheet.write(0,2,'Documento de Identidad')
    worksheet.write(0,3,'Correo Electronico')
    worksheet.write(0,4,'Direccion')
    worksheet.write(0,5,'Telefono')
    worksheet.write(0,6,'Numero de Registro de Contribuyente')
    worksheet.write(0,7,'Giro de Negocio')
    worksheet.write(0,8,'Nombre Comercial')
    worksheet.write(0,9,'Nombre del Contacto')

    n=1 # lineas de encabezado

    # Escribir datos a la hoja de trabajo (worksheet)
    for row in range(len(data)):
        for col in range(len(data[row])):
            worksheet.write(row + n, col, data[row][col])

    # Cerrar el libro (workbook)
    workbook.close()

    # Capturar datos desde el archivo de memoria
    data_to_download = temp_file.getvalue()

    # Preparar la respuesta para descarga (download)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename='+archivo+'.xlsx'
    response.write(data_to_download)

    return response
    #return redirect('client_data_listado')
    #return HttpResponseRedirect('client_data_listado')
    #return HttpResponseRedirect('/client_data/')

    #return render(request, 'client_data/client_data_listado.html')


def Giro_Negocio_To_Excel_1(request):
    context = {
        'archivo': 'GirosNegocio',
    }

    return render(request, 'client_data/giro_negocio_to_excel_1.html', {'context': context})


def Giro_Negocio_To_Excel_2(request):

    queryset_list = Giro_Negocio.objects.values('nombre_giro_negocio','codigo_giro_negocio')
    #contenido del campo archivo
    if 'archivo' in request.GET:
        archivo = request.GET['archivo']

    # Crear un objeto (object) para crear archivos en memoria
    temp_file = BytesIO()

    # Empezar un libro (workbook)
    workbook = xlsxwriter.Workbook(temp_file)
    worksheet = workbook.add_worksheet()
    
    # Prepararar los datos a escribirse
    data = []
    for giro_negocio in queryset_list:
        nombre_giro_negocio=giro_negocio['nombre_giro_negocio']
        codigo_giro_negocio=giro_negocio['codigo_giro_negocio']

        data.append([codigo_giro_negocio, nombre_giro_negocio])


    # Escribir los encabezados de la hoja de trabajo (linea 1)
    worksheet.write(0,0,'Codigo Giro de Negocio')
    worksheet.write(0,1,'Nombre Giro de Negocio')

    n=1 # lineas de encabezado

    # Escribir datos a la hoja de trabajo (worksheet)
    for row in range(len(data)):
        for col in range(len(data[row])):
            worksheet.write(row + n, col, data[row][col])

    # Cerrar el libro (workbook)
    workbook.close()

    # Capturar datos desde el archivo de memoria
    data_to_download = temp_file.getvalue()

    # Preparar la respuesta para descarga (download)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename='+archivo+'.xlsx'
    response.write(data_to_download)

    return response
