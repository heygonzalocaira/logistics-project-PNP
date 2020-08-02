from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class MUserGrado(models.Model):
    codGrado = models.IntegerField()
    Grado = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Clase = models.CharField(max_length=50)
    OrdClase = models.IntegerField()
    Categoria = models.CharField(max_length=50)
    OrdCategoria = models.IntegerField()
    Jerarquia = models.CharField(max_length=50)
    OrdJerarquia = models.IntegerField()
    Estado = models.IntegerField()
    obs = models.TextField()


class MUserRol(models.Model):
    rol = models.CharField(max_length=100)
    Descripcion = models.TextField()
    Estado = models.IntegerField()
    obs = models.TextField()


class MUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cip = models.IntegerField()
    idGrado = models.IntegerField()
    Grado = models.CharField(max_length=50)
    ApePaterno = models.CharField(max_length=50)
    ApeMaterno = models.CharField(max_length=50)
    Nombres = models.CharField(max_length=50)
    Imagen = models.ImageField(upload_to="img/")
    Administrador = models.BooleanField()
    idRol = models.IntegerField()
    activo = models.BooleanField()
    estado = models.IntegerField()
    MotivoBaja = models.TextField()
    obs = models.TextField()


class MtipoDocumento(models.Model):
    Documento = models.CharField(max_length=60)
    nombre_corto = models.CharField(max_length=40)
    activo = models.IntegerField()
    estado = models.IntegerField()
    tipo = models.IntegerField()
    observacion = models.TextField()


class MUbigeo(models.Model):
    departamento = models.CharField(max_length=40)
    provincia = models.CharField(max_length=40)
    distrito = models.CharField(max_length=40)
    estado = models.IntegerField()
    observacion = models.TextField()


class RegDocumentosORI(models.Model):
    unidad_pnp = models.CharField(max_length=60)
    codigo_arequipa = models.IntegerField()
    codigo_lima = models.IntegerField()
    unidad = models.IntegerField()
    descripcion_larga = models.TextField()
    descripcion = models.TextField()
    nombre_corto = models.CharField(max_length=50)
    gran_unidad = models.CharField(max_length=50)
    divisiones = models.CharField(max_length=50)
    tipo_unidad = models.IntegerField()
    id_ubicacion = models.ForeignKey('MUbigeo', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=70)
    telefono = models.IntegerField()
    celular = models.IntegerField()
    correoInstitucional = models.EmailField()
    correoAlterno = models.EmailField()
    redSocial = models.CharField(max_length=80)
    contacto = models.CharField(max_length=80)
    n_orden = models.IntegerField()
    codigo_historico = models.IntegerField()
    activo = models.IntegerField()
    estado = models.IntegerField()
    tipo = models.IntegerField()
    observacion = models.TextField()


class MAreaORI(models.Model):
    area = models.CharField(max_length=50)
    grupo = models.CharField(max_length=50)
    activo = models.IntegerField()
    estado = models.IntegerField()
    tipo = models.IntegerField()
    contacto = models.CharField(max_length=50)
    email = models.EmailField()
    observacion = models.TextField()



class Documentos(models.Model):
    fecha_ingreso = models.DateField()
    id_tipoDocumento = models.ForeignKey('MtipoDocumento', on_delete=models.CASCADE)
    tipoDocumento = models.IntegerField()
    n_documento = models.IntegerField()
    fecha_documento = models.DateField()
    id_unidadEntrega = models.ForeignKey('RegDocumentosORI', on_delete=models.CASCADE)
    unidadEntrega = models.CharField(max_length=80)
    quien_entrega = models.CharField(max_length=80)
    id_area = models.ForeignKey('MAreaORI', on_delete=models.CASCADE)
    area_destino = models.CharField(max_length=50)
    # id_encargado = models.ForeignKey('IPersonalORI', on_delete=models.CASCADE)
    encargado = models.CharField(max_length=60)
    contenido = models.TextField()
    #  id_unidadDestino = models.ForeignKey('RegDocumentosORI', on_delete=models.CASCADE)
    unidad_Destino = models.CharField(max_length=60)
    documento_tramitado = models.CharField(max_length=100)
    fecha_salida = models.DateField()
    archivo = models.CharField(max_length=100)
    ruta = models.FileField(upload_to='Documentos/')
    numero_Hoja = models.IntegerField()
    activo = models.IntegerField()
    estado = models.IntegerField()
    tipo = models.IntegerField()
    observacion = models.TextField()

# class Doc_confidencial(models.Model):
