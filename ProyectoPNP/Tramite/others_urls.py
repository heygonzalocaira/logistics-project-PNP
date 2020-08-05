from .views import login_user, logout_user, index_tramite , historial_tramite
from django.urls import path

urlpatterns = [
    path('', login_user, name='login_user'),
    path('tramite', index_tramite, name='index'),
    path('logout', logout_user, name='logout_user'),
    path('historial', historial_tramite, name='historial_tramite'),
]

