from music_generator.core.models import Note


def generate_notes():
    # chromatic scale
    base_notes = "ABCDEFG"
    sharp_notes = "ACDGF"
    octaves_range = range(0, 8)  # from 0 to 7

    for octave in octaves_range:
        for note in base_notes:
            note_name = f"{note}{octave}"
            Note.objects.get_or_create(
                name=note_name, octave=octave, defaults={"frequency": None},
            )
            if note in sharp_notes:
                note_sharp_name = f"{note}#{octave}"
                Note.objects.get_or_create(
                    name=note_sharp_name, octave=octave, defaults={"frequency": None},
                )


def generate_scales():
    raise NotImplementedError  # TODO


def generate_note_frequencies():
    raise NotImplementedError  # not useful if using Tone.js
