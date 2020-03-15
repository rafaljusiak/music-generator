from django.db import models


class Note(models.Model):
    name = models.CharField(verbose_name="Name", max_length=3,)
    frequency = models.FloatField(verbose_name="Frequency", null=True, blank=True,)
    octave = models.IntegerField(verbose_name="Octave number")

    def __str__(self):
        return self.name


class Scale(models.Model):
    RELATED_NAME = "scales"

    notes = models.ManyToManyField(
        "core.Note",
        verbose_name="Notes",
        related_name=RELATED_NAME,
        related_query_name=RELATED_NAME,
    )
    name = models.CharField(verbose_name="Name", max_length=64,)

    def __str__(self):
        return self.name
