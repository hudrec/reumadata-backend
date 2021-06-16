from django.db import models


class ItemNeuro(models.Model):
    nombre = models.CharField()
    aplica = models.BooleanField()
    localizacion = models.CharField()


class CategoriaNeuro(models.Model):
    nombre = models.CharField()
    aplica = models.BooleanField()
    items = models.ManyToManyField(
        ItemNeuro
    )


class Neuropsiquiatrico(models.Model):
    sistema_nervioso_central = models.ForeignKey(
        CategoriaNeuro
    )
    sistema_nervioso_periferico = models.ForeignKey(
        CategoriaNeuro
    )
    otros_desordenes = models.ForeignKey(
        CategoriaNeuro
    )
    fecha = models.DateTimeField()
