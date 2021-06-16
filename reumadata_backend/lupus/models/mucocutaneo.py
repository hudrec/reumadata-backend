from django.db import models


class ItemMucocutaneo(models.Model):
    nombre = models.CharField()
    aplica = models.BooleanField()
    localizacion = models.CharField()


class CategoriaMucocutaneo(models.Model):
    nombre = models.CharField()
    aplica = models.BooleanField()
    items = models.ManyToManyField(
        ItemMucocutaneo
    )


class Mucocutaneo(models.Model):
    categorias = models.ManyToManyField(
        CategoriaMucocutaneo
    )
    otros = models.ManyToManyField(
        ItemMucocutaneo
    )
    fecha = models.DateTimeField()