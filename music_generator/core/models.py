from django.db import models


class Note(models.Model):
    name = models.CharField(max_length=3)
    frequency = models.IntegerField()


class Scale(models.Model):
    notes = models.ManyToManyField("core.Note")
    name = models.CharField(max_length=64)
