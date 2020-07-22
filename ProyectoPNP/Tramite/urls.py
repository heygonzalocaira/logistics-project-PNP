from rest_framework import routers
from .views_api import DocumentosViewSet, MtipoDocumentoViewSet, RegDocumentosORIViewSet, MAreaORIViewSet, MUbigeoViewSet


router = routers.SimpleRouter()
router.register('Documentos', DocumentosViewSet)
router.register('TipoDocumentos', MtipoDocumentoViewSet)
router.register('RegDocumentosORI', RegDocumentosORIViewSet)
router.register('AreaORI', MAreaORIViewSet)
router.register('Ubigeo', MUbigeoViewSet)

urlpatterns = router.urls
