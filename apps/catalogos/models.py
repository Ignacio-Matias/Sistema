from django.db import models

# Create your models here.
tipopersona = (('DGTIC','DGTIC'),('CONTACTO','CONTACTO'),)
tipouso = (('INTERNO','INTERNO'),('EXTERNO','EXTERNO'),)

class cat_tipo(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.descripcion)

class cat_tecnologias(models.Model):
    descripcion = models.CharField(max_length=50)
    tipo_id = models.ForeignKey(cat_tipo)

class cat_personas (models.Model):
    puc_id = models.IntegerField
    tipo = models.CharField("Tipo de Contacto",max_length=20, choices=tipopersona)

class cat_especialidad (models.Model):
    descripcion = models.CharField(max_length=50)

class cat_estatus(models.Model):
    descripcion = models.CharField(max_length=50)

class cat_documentos(models.Model):
    archivoDescripcion = models.FileField("Documento",upload_to='media',null=True,blank = True )

