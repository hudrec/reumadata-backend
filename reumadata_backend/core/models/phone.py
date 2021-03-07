from django.db import models

from django.utils.translation import ugettext_lazy as _
from core import constants
# Create your models here.


class Phone(models.Model):
    number = models.CharField(
        _("Número de teléfono"),
        max_length=255,
        blank=True,
    )
    type = models.CharField(
        verbose_name=_("Tipo de número telefónico"),
        max_length=2,
        choices=constants.PHONE_TYPE_CHOICES,
    )

    def __str__(self):
        return self.number