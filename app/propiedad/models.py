from django.db import models


class TipoPropiedad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Propiedad(models.Model):
    id = models.BigAutoField(primary_key=True)
    calle = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=255, blank=True, null=True)
    tipoPropiedad = models.ForeignKey(TipoPropiedad, models.DO_NOTHING, blank=True, null=True)
