from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from core.models import ItemModel


class ItemComorbidity(ItemModel):
    start_date = models.DateField(
        _("Fecha de inicio"),
        default=timezone.now,
    )
    end_date = models.DateField(
        _("Fecha de fin"),
        default=timezone.now,
        blank=True,
        null=True,
    )
    treatment = models.CharField(
        verbose_name=_("Tratamiento"),
        blank=True,
        max_length=1275,
    )

    def __str__(self):
        return self.name

