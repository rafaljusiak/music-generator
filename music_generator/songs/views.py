from django.urls import reverse_lazy
from django.views import generic

from music_generator.core.enums import NoteDurations
from music_generator.core.models import Scale
from music_generator.songs.forms import SongForm
from music_generator.songs.generator import create_track


class SongView(generic.FormView):
    template_name = "songs/song.html"
    success_url = reverse_lazy("song")
    form_class = SongForm

    def get_initial(self):
        initial = super().get_initial()
        query_params = self.request.GET.copy()
        parsed_params = dict([(k, int(v)) for k, v in query_params.items()])
        initial.update(**parsed_params)
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query_params = self.request.GET
        scale_id = query_params.get("scale", None)
        scale = (
            Scale.objects.get(id=scale_id)
            if scale_id is not None
            else Scale.objects.order_by("?").first()
        )

        settings = {
            "length": int(query_params.get("length", 8)),
            "min_octave": int(query_params.get("min_octave", 4)),
            "max_octave": int(query_params.get("max_octave", 4)),
            "tempo": int(query_params.get("tempo", 60)),
            "shortest_note": int(
                query_params.get("shortest_note", NoteDurations.EIGHTH_NOTE.value)
            ),
            "longest_note": int(
                query_params.get("longest_note", NoteDurations.HALF_NOTE.value)
            ),
            "scale": scale,
        }
        context.update(
            {
                "request": self.request,
                "track_synth": create_track(**settings),
                **settings,
            }
        )
        return context
