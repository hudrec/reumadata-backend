from django.db import models


class ItemOto(models.Model):
    nombre = models.CharField()
    aplica = models.BooleanField()
    info = models.CharField()


class Otorrinolaringologico(models.Model):
    items = models.ForeignKey(
        ItemOto
    )
    fecha = models.DateTimeField()