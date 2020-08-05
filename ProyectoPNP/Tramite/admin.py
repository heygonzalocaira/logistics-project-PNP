from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "Administrador de PNP"
admin.site.site_title = "Portal de Administración"
admin.site.index_title = "Bienvenidos al portal de administración"

admin.site.register(MUser)
admin.site.register(MtipoDocumento)
admin.site.register(MAreaORI)
