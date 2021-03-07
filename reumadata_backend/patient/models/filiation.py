from django.db import models
from core.models import Ubigeo, Ethnicity, Phone
from django.utils.translation import ugettext_lazy as _
from patient import constants
# Create your models here.


class Filiation(models.Model):
    first_name = models.CharField(
        verbose_name=_("Nombres"),
        max_length=255,
    )
    last_name = models.CharField(
        verbose_name=_("Apellidos"),
        max_length=255,
    )
    gender = models.CharField(
        verbose_name=_("Género"),
        max_length=2,
        choices=constants.GENDER_CHOICES,
    )
    medical_history_number = models.CharField(
        verbose_name=_("Número de historia clínica"),
        max_length=50,
        blank=True,
    )
    dni = models.CharField(
        _("DNI"),
        max_length=12,
    )
    date_birth = models.DateTimeField(
        verbose_name=_("Fecha de Nacimiento"),
    )
    place_birth = models.ForeignKey(
        Ubigeo,
        null=True,
        related_name='pb_filiations',
        verbose_name=_("Lugar de Nacimiento"),
        on_delete=models.SET_NULL,
    )
    place_origin = models.ForeignKey(
        Ubigeo,
        null=True,
        related_name='po_filiations',
        verbose_name=_("Lugar de Prodencia"),
        on_delete=models.SET_NULL,
    )
    ethnicity = models.ForeignKey(
        Ethnicity,
        null=True,
        verbose_name=_("Etnia"),
        on_delete=models.SET_NULL,
    )
    degree = models.CharField(
        verbose_name=_("Grado de Instrucción"),
        max_length=2,
        choices=constants.DEGREE_CHOICES,
    )
    marital_status = models.CharField(
        verbose_name=_("Estado Civil"),
        max_length=2,
        choices=constants.MARITAL_STATUS_CHOICES,
    )
    occupation = models.CharField(
        verbose_name=_("Ocupación"),
        max_length=255,
        blank=True,
    )
    religion = models.CharField(
        verbose_name=_("Religion"),
        max_length=255,
        blank=True,
    )
    phone = models.ManyToManyField(
        Phone,
        blank=True,
        verbose_name=_("Números de telefono"),
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name






