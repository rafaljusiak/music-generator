from django.views import generic


class SongView(generic.TemplateView):
    template_name = "songs/song.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "track_synth": [
                    {"time": 0, "note": "C3", "velocity": 0.9},
                    {"time": 1, "note": "C4", "velocity": 0.5},
                    {"time": 2, "note": "C3", "velocity": 0.5},
                ],
            }
        )
        return context
