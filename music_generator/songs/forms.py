from django import forms

from music_generator.core.enums import NOTE_DURATIONS_CHOICES, NoteDurations
from music_generator.core.models import Scale


class SongForm(forms.Form):
    scale = forms.ModelChoiceField(queryset=Scale.objects.all(), empty_label=None)
    length = forms.IntegerField(min_value=2, max_value=32, initial=8)
    min_octave = forms.IntegerField(min_value=0, max_value=7, initial=4)
    max_octave = forms.IntegerField(min_value=0, max_value=7, initial=4)
    shortest_note = forms.ChoiceField(
        choices=NOTE_DURATIONS_CHOICES, initial=NoteDurations.EIGHTH_NOTE.value
    )
    longest_note = forms.ChoiceField(
        choices=NOTE_DURATIONS_CHOICES, initial=NoteDurations.HALF_NOTE.value
    )
    tempo = forms.IntegerField(min_value=30, max_value=180, initial=60)
