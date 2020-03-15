from django.core.management.base import BaseCommand

from music_generator.core.setup import generate_scales, generate_notes


class Command(BaseCommand):
    help = "Generates base data (notes and scales)"

    def handle(self, *args, **options):
        generate_notes()
        generate_scales()
