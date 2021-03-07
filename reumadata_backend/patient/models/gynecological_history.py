from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from core.models import ItemModel


class GinecologyComplication(models.Model):
    name = models.CharField(
        verbose_name=_("Nombre"),
        max_length=255,
    )
    is_active = models.BooleanField(
        verbose_name=_("Aplica"),
        default=False
    )
    register_date = models.DateField(
        verbose_name=_("Fecha de Registro"),
        default=timezone.now,
    )
    is_custom = models.BooleanField(
        verbose_name=_("Personalizada"),
        default=True
    )

    def __str__(self):
        return self.name


class GynecologicalHistory(models.Model):
    obstetric_gyneco_history = models.ManyToManyField(
        ItemModel,
        verbose_name=_("Antecedentes gineco-obstetricos"),
    )
    pregnancy_complications = models.ManyToManyField(
        GinecologyComplication,
        related_name='pc_histories',
        verbose_name=_("Complicaciones durante la Gestación"),
    )
    birth_complications = models.ManyToManyField(
        GinecologyComplication,
        related_name='bc_histories',
        verbose_name=_("Complicaciones durante el parto "),
    )