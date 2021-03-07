from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from patient import constants


class BooleanText(models.Model):
    is_active = models.BooleanField(
        verbose_name=_("Aplica"),
        default=False
    )
    register_date = models.DateField(
        verbose_name=_("Fecha de Registro"),
        default=timezone.now,
    )
    description = models.CharField(
        verbose_name=_("Descripción"),
        null=True,
        blank=True,
        max_length=1275,
    )


class ItemModel(models.Model):
    name = models.CharField(
        verbose_name=_("Nombre"),
        max_length=255,
    )
    is_active = models.BooleanField(
        verbose_name=_("¿Aplica?"),
        default=False
    )
    register_date = models.DateField(
        verbose_name=_("Fecha de Registro"),
        default=timezone.now,
    )
    is_custom = models.BooleanField(
        verbose_name=_("¿Es personalizada?"),
        default=True
    )
    value = models.IntegerField(
        verbose_name=_("Tiempo o valor"),
        default=0
    )
    value_type = models.CharField(
        verbose_name=_("Unidad de medida"),
        max_length=2,
        choices=constants.VALUE_TYPE_CHOICE
    )

    def __str__(self):
        return self.name