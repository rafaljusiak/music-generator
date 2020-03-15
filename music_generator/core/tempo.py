from music_generator.core.enums import NoteDurations


def get_notes_durations(
    tempo,
    shortest=NoteDurations.SIXTEENTH_NOTE.value,
    longest=NoteDurations.WHOLE_NOTE.value,
):
    durations = []
    for d in NoteDurations:
        if longest >= d.value >= shortest:
            durations.append(d.value / tempo)
    return durations
