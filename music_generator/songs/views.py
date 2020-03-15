from django.views import generic

from music_generator.songs.generator import create_track


class SongView(generic.TemplateView):
    template_name = "songs/song.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        length = 8
        context.update(
            {"track_synth": create_track(length=length, min_octave=3, max_octave=4,),}
        )
        return context
