from django.db import models

from django.utils.translation import ugettext_lazy as _
# Create your models here.

PHONE_TYPE_CHOICES = (
    ('C', 'Celular'),
    ('F', 'Fijo'),
)


class Phone(models.Model):
    number = models.CharField(
        _("Número de teléfono"),
        max_length=255,
        blank=True,
    )
    type = models.CharField(
        verbose_name=_("Grado de Instrucción"),
        max_length=2,
        choices=PHONE_TYPE_CHOICES,
    )

    def __str__(self):
        return self.number