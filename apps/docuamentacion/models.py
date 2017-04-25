from django.db import models

# Create your models here.

#encoding:utf-8
from django.db import migrations,models
from apps.catalogos.models import *

# para  ficha
class credenciales(models.Model):
    cat_tipo_id = models.ForeignKey(cat_tecnologias)
    usuario = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20)
    host = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    puerto = models.CharField(max_length=5)

class ficha (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    cat_estatus_id = models.ForeignKey(cat_estatus)
    url = models.CharField(max_length=50)
    git = models.CharField(max_length=50)
    contacto_id = models.ForeignKey(cat_personas)
    tipouso = models.CharField("Tipo de uso",max_length=20, choices=tipouso)
    dependencia_id = models.IntegerField
    credencial_id = models.ManyToManyField(credenciales)

class equipo_ficha (models.Model):
    ficha_id = models.ForeignKey(ficha)
    cat_personas_id = models.ForeignKey(cat_personas)
    cat_especialidad_id = models.ForeignKey(cat_especialidad)

class ficha_cat_tecnologias(models.Model):
    ficha_id = models.ForeignKey(ficha)
    cat_tecnologias_id = models.ForeignKey(cat_tecnologias)
    version = models.CharField(max_length = 10)


class documento_archivo(models.Model):
    ficha_id = models.ForeignKey(ficha)
    cat_documento_id = models.ForeignKey(cat_documentos)
    # archivo

class logtable (models.Model):
    usuario_id = models.IntegerField
    fecha = models.DateField
    nametabla = models.CharField(max_length=50)
    registro_id = models.IntegerField
    tipomovimiento = models.CharField(max_length=50)