import random

from music_generator.core.models import Note


def create_song():
    pass


def create_track(scale, length=8, min_octave=4, max_octave=4):
    notes_range = range(length)
    octave_range = range(min_octave, max_octave + 1)
    track = []

    notes = list(Note.objects.filter(scales=scale))

    for _ in notes_range:
        octave = random.choice(octave_range)
        track.append(
            {
                "time": _,  # TODO use notes length
                "note": random.choice(notes).name_with_octave(octave),
                "velocity": 0.7,
            }
        )

    return track
