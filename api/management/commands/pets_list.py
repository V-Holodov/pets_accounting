from django.core.management.base import BaseCommand

from api.models import Pet
from api.serializers import PetSerializer


class Command(BaseCommand):
    help = "Displaying a list of pets in stdout"

    def add_arguments(self, parser):
        parser.add_argument(
            "--has-photos", action="store_true", help="Returns entries with photos"
        )

    def handle(self, *args, **kwargs):
        has_photos = kwargs["has_photos"]

        if has_photos:
            pets = Pet.objects.filter(photos__isnull=False)
        else:
            pets = Pet.objects.filter(photos__isnull=True)
        serializer = PetSerializer(pets, many=True)
        self.stdout.write(f"{serializer}")
