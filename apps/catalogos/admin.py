from django.contrib import admin
from apps.catalogos.models import *
# Register your models here.
admin.site.register(cat_tipo)
admin.site.register(cat_tecnologias)
admin.site.register(cat_estatus)
admin.site.register(cat_especialidad)