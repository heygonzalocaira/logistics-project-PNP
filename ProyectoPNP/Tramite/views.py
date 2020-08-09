from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
from .models import *


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['uname']
            password = request.POST['psw']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # return redirect('admin/')
                return redirect(reverse('index'))
            else:
                return render(request, 'vistas/login.html', {'message': "El usuario o la contraseña es incorrecto"})
        else:
            return render(request, 'vistas/login.html')
    else:
        return redirect(reverse('index'))


@login_required
def logout_user(request):
    logout(request)
    return redirect('/')


@login_required
def index_tramite(request):
    return render(request, 'vistas/index.html')


@login_required
def tramite_historial(request):
    return render(request, 'vistas/historial.html')


@login_required
def tramite_reportes(request):
    return render(request, 'vistas/reportes.html')


@login_required
def save_documento(request):
    if request.method == 'POST':
        clasificacion = request.POST['clasificacion_index']
        fecha_ingreso = request.POST['f_ingreso_index']
        tipo_documento = request.POST['t_documento_index']
        nro_doc = request.POST['n_hoja_index']
        fecha_document = request.POST['d_salida_index']
        encargado_ent = request.POST['encargado_index']
        unidadrem = request.POST['u_remitente_index']
        id_area = request.POST['a_destino_index']
        nombre_area = request.POST['area_nombre_index']
        encargado = request.POST['encargado_2']
        asunto = request.POST['t_asunto']
        unidadDestino = request.POST['u_destino_2']
        fec_salida = request.POST['f_salida_index']
        nro_hoja = request.POST['n_hoja_index']
        observaciones = request.POST['t_observaciones']
        documennt = Documentos(fecha_ingreso=fecha_ingreso,
                               id_tipoDocumento=MtipoDocumento.objects.get(id=tipo_documento),
                               tipoDocumento=tipo_documento,
                               n_documento=nro_doc,
                               fecha_documento=fecha_document,
                               unidadEntrega=unidadrem,
                               quien_entrega=encargado_ent,
                               id_area=MAreaORI.objects.get(id=id_area),
                               area_destino=nombre_area,
                               encargado=encargado,
                               contenido=asunto,
                               unidad_Destino=unidadDestino,
                               fecha_salida=fec_salida,
                               numero_Hoja=nro_hoja,
                               activo=1,
                               estado=1,
                               tipo=1,
                               observacion=observaciones)
        documennt.save()
        return redirect('/')

    return HttpResponse("Pagina inexistente", status=404)
