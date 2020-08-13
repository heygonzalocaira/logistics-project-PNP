from .views import *
from django.urls import path

urlpatterns = [
    path('', login_user, name='login_user'),
    path('tramite', index_tramite, name='index'),
    path('tramite/historial', tramite_historial, name='t_historial'),
    path('tramite/reportes', tramite_reportes, name='t_reportes'),
    path('tramite/save', save_documento, name='doc_save'),
    path('logout', logout_user, name='logout_user'),
]

