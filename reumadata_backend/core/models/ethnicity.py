from django.db import models

from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Ethnicity(models.Model):
    name = models.CharField(
        _("Etnia"),
        max_length=255,
    )

    def __str__(self):
        return self.name