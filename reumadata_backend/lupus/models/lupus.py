from django.db import models
from reumadata_backend.patient.models import Patient


class AtencionLupus():
    lupus = models.ForeignKey(Lupus)
    fecha = models.DateTimeField


class Lupus(models.Model):
    patient = models.ForeignKey(Patient)
    manifestaciones_sistemicas = models.ManyToManyField(ManifestacionesSistemicas)
    mucocutaneo = models.ManyToManyField(Mucocutaneo)
    musculoesqueletico = models.ManyToManyField(Musculoesqueletico)
    neuropsiquiatrico = models.ManyToManyField(Neuropsiquiatrico)
    otorrinolaringologico = models.ManyToManyField(Otorrinolaringologico)
    respiratorio = models.ManyToManyField(Respiratorio)
    cardiovascular = models.ManyToManyField(Cardiovascular)
    gastrointestinal = models.ManyToManyField(Gastrointestinal)
    oftalmologico = models.ManyToManyField(Oftalmologico)
    renal = models.ManyToManyField(Renal)
    hematologico = models.ManyToManyField(hematologico)
    biopsia = models.ManyToManyField(Biopsia)
    imagenes = models.ManyToManyField(Imagenes)
    pruebas_pulmonares = models.ManyToManyField(PruebasPulmonares)
    pruebas_oftalmologicas = models.ManyToManyField(PruebasOftalmologicas)
    otros_estudios = models.ManyToManyField(OtrosEstudios)
    criterios_clasificacion = models.ManyToManyField(CriteriosClasificacion)
    indice_actividad = models.ManyToManyField(IndiceActividad)
    indice_danio = models.ManyToManyField(IndiceDanio)
    tratamiento = models.ManyToManyField(Tratamiento)

