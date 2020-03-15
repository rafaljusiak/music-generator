from django.contrib import admin

from music_generator.core.models import Note, Scale


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass


@admin.register(Scale)
class ScaleAdmin(admin.ModelAdmin):
    pass
