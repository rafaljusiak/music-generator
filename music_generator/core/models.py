from django.db import models

from music_generator.core.enums import ScaleTypes


class Note(models.Model):
    index = models.IntegerField(verbose_name="Index", unique=True)
    name = models.CharField(verbose_name="Name", max_length=3, unique=True,)
    is_sharp = models.BooleanField(verbose_name="Is sharp")
    frequency = models.FloatField(verbose_name="Frequency", null=True, blank=True,)

    def name_with_octave(self, octave=4):
        return f"{self.name}{octave}"

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
    name = models.CharField(verbose_name="Name", max_length=64, unique=True)
    scale_type = models.CharField(
        verbose_name="Type", max_length=32, choices=[(t, t.value) for t in ScaleTypes]
    )

    def __str__(self):
        return self.name
