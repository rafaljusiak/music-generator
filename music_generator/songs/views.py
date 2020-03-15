from django.views import generic

from music_generator.core.models import Scale
from music_generator.songs.generator import create_track


class SongView(generic.TemplateView):
    template_name = "songs/song.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        length = 8
        min_octave = 4
        max_octave = 4
        scale = Scale.objects.order_by("?").first()
        context.update(
            {
                "scale": scale,
                "track_synth": create_track(
                    scale=scale,
                    length=length,
                    min_octave=min_octave,
                    max_octave=max_octave,
                ),
            }
        )
        return context
