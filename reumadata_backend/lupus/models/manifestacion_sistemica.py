from django.db import models


class PerdidaPeso(models.Model):
    peso = models.FloatField()
    talla = models.FloatField()
    imc = models.FloatField()
    estado = models.CharField()


class ItemMS(models.Model):
    nombre = models.CharField()
    aplica = models.BooleanField()
    description = models.CharField()


class ManifestacionSistemica(models.Model):
    items = models.ForeignKey(
        ItemMS
    )
    perdida_peso = models.ForeignKey(
        PerdidaPeso
    )
    otros = models.ManyToManyField(
        ItemMS
    )
    fecha = models.DateTimeField()






