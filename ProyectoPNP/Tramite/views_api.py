from rest_framework import viewsets

from .models import MtipoDocumento, MUbigeo, RegDocumentosORI, MAreaORI, Documentos
from .serializer import MtipoDocumentoSerializer, RegDocumentosORISerializer, MAreaORISerializer, DocumentosSerializer, MUbigeoSerializer


class DocumentosViewSet(viewsets.ModelViewSet):
    queryset = Documentos.objects.all()
    serializer_class = DocumentosSerializer


class MtipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = MtipoDocumento.objects.all()
    serializer_class = MtipoDocumentoSerializer


class RegDocumentosORIViewSet(viewsets.ModelViewSet):
    queryset = RegDocumentosORI.objects.all()
    serializer_class = RegDocumentosORISerializer


class MAreaORIViewSet(viewsets.ModelViewSet):
    queryset = MAreaORI.objects.all()
    serializer_class = MAreaORISerializer


class MUbigeoViewSet(viewsets.ModelViewSet):
    queryset = MUbigeo.objects.all()
    serializer_class = MUbigeoSerializer
