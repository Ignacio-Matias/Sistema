from django.contrib import admin

# Register your models here.
from apps.docuamentacion.models import *

admin.site.register(credenciales)
admin.site.register(ficha)
admin.site.register(equipo_ficha)
admin.site.register(ficha_cat_tecnologias)
admin.site.register(documento_archivo)
admin.site.register(logtable)