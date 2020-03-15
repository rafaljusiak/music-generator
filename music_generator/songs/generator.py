import random

from music_generator.core.models import Note


def create_song():
    pass


def create_track(length=8, scale=None, min_octave=4, max_octave=4):
    notes_range = range(length)
    track = []

    notes = list(
        Note.objects.filter(
            octave__gte=min_octave, octave__lte=max_octave, scales=scale,
        )
    )

    for _ in notes_range:
        track.append(
            {
                "time": _,  # TODO use notes length
                "note": random.choice(notes).name,
                "velocity": 0.7,
            }
        )

    return track
