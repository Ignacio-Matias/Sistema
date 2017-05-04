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

    def __str__(self):
        return '{}'.format(self.descripcion)

class cat_personas(models.Model):
    puc_id = models.IntegerField(blank=True, null=True)
    tipo = models.CharField("Tipo de Contacto", max_length=20, choices=tipopersona)

    def __str__(self):
        return '{}'.format(self.tipo)

class cat_especialidad (models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.descripcion)

class cat_estatus(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.descripcion)

class cat_documentos(models.Model):
    archivoDescripcion = models.FileField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.archivoDescripcion)