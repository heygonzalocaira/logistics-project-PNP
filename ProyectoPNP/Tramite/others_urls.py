from .views import login_user, logout_user, index_tramite, tramite_historial, tramite_reportes
from django.urls import path

urlpatterns = [
    path('', login_user, name='login_user'),
    path('tramite', index_tramite, name='index'),
    path('tramite/historial', tramite_historial, name='t_historial'),
    path('tramite/reportes', tramite_reportes, name='t_reportes'),
    path('logout', logout_user, name='logout_user'),
    path('historial', historial_tramite, name='historial_tramite'),
]

