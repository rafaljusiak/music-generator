from django import forms

from music_generator.core.models import Scale


class SongForm(forms.Form):
    scale = forms.ModelChoiceField(queryset=Scale.objects.all())
    length = forms.IntegerField(min_value=2, max_value=32, initial=8)
    min_octave = forms.IntegerField(min_value=0, max_value=7, initial=4)
    max_octave = forms.IntegerField(min_value=0, max_value=7, initial=4)
