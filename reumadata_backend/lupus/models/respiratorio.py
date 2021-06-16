from django.db import models


class ItemRespiratorio(models.Model):
    nombre = models.CharField()
    aplica = models.BooleanField()
    info = models.CharField()


class CategoriaRespiratorio(models.Model):
    nombre = models.CharField()
    aplica = models.BooleanField()
    items = models.ManyToManyField(
        ItemRespiratorio
    )


class Respiratorio(models.Model):
    pleural = models.ForeignKey(
        CategoriaRespiratorio
    )
    parenquimal = models.ForeignKey(
        CategoriaRespiratorio
    )
    otros = models.ForeignKey(
        ItemRespiratorio
    )
    fecha = models.DateTimeField()
