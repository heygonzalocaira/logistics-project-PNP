from rest_framework import serializers
from .models import MtipoDocumento, MUbigeo, RegDocumentosORI, MAreaORI, Documentos


class MtipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MtipoDocumento
        fields = [
            'Documento',
            'nombre_corto',
            'activo',
            'estado',
            'tipo',
            'observacion',
        ]


class RegDocumentosORISerializer(serializers.ModelSerializer):
    class Meta:
        model = RegDocumentosORI
        fields = [
            'unidad_pnp',
            'codigo_arequipa',
            'codigo_lima',
            'unidad',
            'descripcion_larga',
            'descripcion',
            'nombre_corto',
            'gran_unidad',
            'divisiones',
            'tipo_unidad',
            'id_ubicacion',
            'direccion',
            'telefono',
            'celular',
            'correoInstitucional',
            'correoAlterno',
            'redSocial',
            'contacto',
            'n_orden',
            'codigo_historico',
            'activo',
            'estado',
            'tipo',
            'observacion',
        ]


class MAreaORISerializer(serializers.ModelSerializer):
    class Meta:
        model = MAreaORI
        fields = [
            'area',
            'grupo',
            'activo',
            'estado',
            'tipo',
            'contacto',
            'email',
            'observacion',
        ]


class MUbigeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MUbigeo
        fields = [
            'departamento',
            'provincia',
            'distrito',
            'estado',
            'observacion',
        ]


class DocumentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentos
        fields = [
            'fecha_ingreso',
            'id_tipoDocumento',
            'tipoDocumento',
            'n_documento',
            'fecha_documento',
            'id_unidadEntrega',
            'unidadEntrega',
            'quien_entrega',
            'id_area',
            'area_destino',
            'encargado',
            'contenido',
            'unidad_Destino',
            'documento_tramitado',
            'fecha_salida',
            'archivo',
            'ruta',
            'numero_Hoja',
            'activo',
            'estado',
            'tipo',
            'observacion',
        ]


