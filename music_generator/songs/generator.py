import random

from music_generator.core.enums import NoteDurations
from music_generator.core.models import Note
from music_generator.core.tempo import get_notes_durations


def create_song():
    pass  # TODO create song from multiple tracks


def create_track(
    scale,
    length=8,
    min_octave=4,
    max_octave=4,
    longest_note=NoteDurations.HALF_NOTE,
    shortest_note=NoteDurations.EIGHTH_NOTE,
    tempo=60,  # whole notes per minute
):
    notes_range = range(length)
    octave_range = range(min_octave, max_octave + 1)
    track = []

    notes = list(Note.objects.filter(scales=scale))
    durations = get_notes_durations(tempo, shortest=shortest_note, longest=longest_note)

    time = 0
    for _ in notes_range:
        octave = random.choice(octave_range)
        duration = random.choice(durations)
        track.append(
            {
                "time": time,
                "note": random.choice(notes).name_with_octave(octave),
                "velocity": 0.7,
                "duration": duration,
            }
        )
        time += duration

    return track
