from enum import Enum


class ScaleTypes(Enum):
    CHROMATIC = "chromatic"
    OCTATONIC = "octatonic"
    HEPTATONIC = "heptatonic"
    HEXATONIC = "hexatonic"
    PENTATONIC = "pentatonic"
    TETRATONIC = "tetratonic"
    MONOTONIC = "monotonic"


SCALE_TYPES_CHOICES = [(t, t.value) for t in ScaleTypes]


class NoteDurations(Enum):
    WHOLE_NOTE = 64
    HALF_NOTE = 32
    QUARTER_NOTE = 16
    EIGHTH_NOTE = 8
    SIXTEENTH_NOTE = 4


NOTE_DURATIONS_CHOICES = [(t.value, t) for t in NoteDurations]
