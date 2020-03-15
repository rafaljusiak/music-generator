from music_generator.core.enums import ScaleTypes
from music_generator.core.models import Note, Scale


def generate_notes():
    # chromatic scale
    base_notes = "ABCDEFG"
    sharp_notes = "ACDGF"
    index = -1
    for note_name in base_notes:
        index += 1
        Note.objects.get_or_create(
            name=note_name, index=index, is_sharp=False, defaults={"frequency": None},
        )
        if note_name in sharp_notes:
            index += 1
            note_sharp_name = f"{note_name}#"
            Note.objects.get_or_create(
                name=note_sharp_name,
                index=index,
                is_sharp=True,
                defaults={"frequency": None},
            )


def generate_scales():
    # TODO add more scales
    scales = [
        {
            "name": "whole tone",
            "notes": "C D E F# G# A#",
            "scale_type": ScaleTypes.HEXATONIC,
        },
        {
            "name": "blues",
            "notes": "A# C D# F F# G",
            "scale_type": ScaleTypes.HEXATONIC,
        },
        {
            "name": "C-major",
            "notes": "C D E F G A B",
            "scale_type": ScaleTypes.HEPTATONIC,
        },
        {
            "name": "C-minor",
            "notes": "C D D# F G G# A#",
            "scale_type": ScaleTypes.HEPTATONIC,
        },
        {
            "name": "chromatic",
            "notes": "A A# B C C# D D# E F F# G G#",
            "scale_type": ScaleTypes.CHROMATIC,
        },
    ]
    for scale in scales:
        scale_instance, _ = Scale.objects.get_or_create(
            name=scale.get("name"), scale_type=scale.get("scale_type")
        )
        notes_list = scale.get("notes").split(" ")
        notes_ids = Note.objects.filter(name__in=notes_list).values_list(
            "id", flat=True
        )
        scale_instance.notes.set(notes_ids)


def generate_note_frequencies():
    raise NotImplementedError  # not useful if using Tone.js
