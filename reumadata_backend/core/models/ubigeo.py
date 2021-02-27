from django.db import models

from django.utils.translation import ugettext_lazy as _

NACIONALITY_CHOICES = (
    ('P', 'Peru'),
    ('E', 'Extranjero'),
)


class State(models.Model):
    name = models.CharField(
        _("Departamento"),
        max_length=255,
        blank=True,
    )

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(
        _("Provincia"),
        max_length=255,
        blank=True,
    )
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name='provinces'
    )

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(
        _("Distrito"),
        max_length=255,
        blank=True,
    )
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name='department_districs'
    )
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name='province_districs'

    )

    def __str__(self):
        return self.name


class Ubigeo(models.Model):
    country = models.CharField(
        _("Pais"),
        max_length=2,
        choices=NACIONALITY_CHOICES,
    )
    district =models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        related_name='ubigeos',
        blank=True,
        null=True
    )


