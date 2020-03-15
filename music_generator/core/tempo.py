from music_generator.core.enums import NoteDurations


def get_notes_durations(
    tempo, shortest=NoteDurations.SIXTEENTH_NOTE, longest=NoteDurations.WHOLE_NOTE
):
    durations = []
    for d in NoteDurations:
        if longest.value >= d.value >= shortest.value:
            durations.append(d.value / tempo)
    return durations
