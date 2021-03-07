from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .filiation import Filiation
from .comorbidity import ItemComorbidity
from .gynecological_history import GynecologicalHistory

from core.models import BooleanText, ItemModel
from patient import constants


class ToxicHabit(ItemModel):
    moment = models.CharField(
        verbose_name=_("Momento del hábito"),
        max_length=2,
        choices=constants.MOMENT_TYPE_CHOICES,
    )

    def __str__(self):
        return self.name


class Immunization(ItemModel):
    immunization_date = models.DateField(
        verbose_name=_("Fecha de Registro"),
        default=timezone.now,
    )
    observation = models.CharField(
        verbose_name=_("Observación "),
        max_length=1255,
        blank=True
    )

    def __str__(self):
        return self.name


class Mortality(models.Model):
    is_active = models.BooleanField(
        verbose_name=_("Aplica"),
        default=False
    )
    death_date = models.DateField(
        verbose_name=_("Fecha de Muerte"),
        default=timezone.now,
    )
    disease = models.CharField(
        verbose_name=_("Enfermedad"),
        blank=True,
        max_length=255
    )
    cause = models.CharField(
        verbose_name=_("Causa de muerte"),
        blank=True,
        max_length=1275,
    )

    def __str__(self):
        return self.name


class Patient(models.Model):
    filiation = models.ForeignKey(
        Filiation,
        verbose_name=_("Filiación"),
        on_delete=models.CASCADE
    )
    # COMORBIDITY
    comorbidity = models.ManyToManyField(
        ItemComorbidity,
        verbose_name=_("Comorbilidad"),
    )
    # ALLERGIC REACTION TO MEDICINES
    allergic_reactions = models.ManyToManyField(
        BooleanText,
        verbose_name=_("Reacciones alergica"),
        related_name='ar_patients',
    )
    # OBSTETRIC gynecological HISTORY
    gyneco_obstetric_history = models.ForeignKey(
        GynecologicalHistory,
        verbose_name=_("Antecedentes Gineco-obstetricos"),
        on_delete=models.SET_NULL,
        null=True,
    )
    # HISTORY OF AUTOIMMUNE DISEASES IN FAMILY MEMBERS
    family_autoimmune_diseases = models.ManyToManyField(
        BooleanText,
        related_name='fad_patients',
        verbose_name=_("Antecedentes de Enfermedades autoinmunes en familiares"),
    )
    # TOXIC HABITS
    toxic_habits = models.ManyToManyField(
        ToxicHabit,
        verbose_name=_("Hábitos tóxicos"),
    )
    # IMMUNIZATIONS
    immunizations = models.ManyToManyField(
        Immunization,
        verbose_name=_("Inmunizaciones"),
    )
    # MORTALITY
    mortality = models.ForeignKey(
        Mortality,
        verbose_name=_("Mortalidad"),
        null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = "Paciente"
