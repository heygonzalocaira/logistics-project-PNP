from .views import *
from django.urls import path

urlpatterns = [
    path('', login_user, name='login_user'),
    path('tramite', index_tramite, name='index'),
    path('tramite/historial', listar_documentos, name='t_historial'),
    path('tramite/reportes', tramite_reportes, name='t_reportes'),
    path('tramite/save', save_documento, name='doc_save'),
    path('logout', logout_user, name='logout_user'),
    path('tramite/eliminar/<int:id>', docu_eliminar, name='delete_doc'),
    path('tramite/eliminar2/<int:id>', docu_eliminar2, name='delete_doc2'),

]

