from django.db import models


class Articulacion(models.Model):
    tipo = models.CharField()
    total = models.IntegerField()
    zonas = models.JSONField()


class ItemMusculoesqueletico(models.Model):
    nombre = models.CharField()
    aplica = models.BooleanField()
    localizacion = models.CharField()


class Musculoesqueletico(models.Model):
    compromiso_articular = models.ManyToManyField(
        Articulacion
    )
    compromiso_muscular = models.ManyToManyField(
        ItemMusculoesqueletico
    )
    otros = models.ManyToManyField(
        ItemMusculoesqueletico
    )
    fecha = models.DateTimeField()